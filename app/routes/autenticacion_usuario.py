# app/routes/autenticacion_usuario.py

import io
import datetime
import logging
import base64

from flask import current_app, request
from flask_restful import Resource
from PIL import Image
import numpy as np
import face_recognition
import jwt

from app.models.usuario import Usuario
from app.services.embedding_storage import obtener_embeddings_en_memoria

log = logging.getLogger(__name__)

class AutenticacionUsuario(Resource):
    """
    POST /usuarios/validate-photo
    multipart/form-data:
        imagen: archivo de imagen

    Flujo:
      1. Validar que llegue el archivo.
      2. Cargar con PIL y forzar a RGB 8-bit.
      3. Asegurar memoria C-contigua.
      4. Extraer face-encoding.
      5. Cargar embeddings de BD en memoria.
      6. Comparar contra cada vector.
      7. Devolver 200+JWT si hay match; 400/401 según corresponda.
    """

    def post(self):
        # 1) Verificar que venga la imagen
        if 'imagen' not in request.files:
            return {'mensaje': 'Imagen no enviada'}, 400

        # 2) Leer y convertir a array RGB
        img_file  = request.files['imagen']
        img_bytes = img_file.read()
        try:
            with Image.open(io.BytesIO(img_bytes)) as img:
                rgb_img = img.convert("RGB")
                arr     = np.asarray(rgb_img, dtype=np.uint8)
        except Exception as e:
            log.error(f"Error procesando imagen con PIL: {e}", exc_info=True)
            return {'mensaje': 'Formato de imagen no soportado'}, 400

        # 3) Forzar copia C-contigua
        arr = np.ascontiguousarray(arr, dtype=np.uint8)
        log.debug(f"[VALIDATE] dtype={arr.dtype}, shape={arr.shape}, contig={arr.flags['C_CONTIGUOUS']}")

        # 4) Extraer embeddings faciales
        try:
            encodings = face_recognition.face_encodings(arr)
        except Exception as e:
            log.error(f"Error en face_encodings: {e}", exc_info=True)
            return {'mensaje': 'No se pudo procesar la imagen'}, 400

        if not encodings:
            return {'mensaje': 'No se detectó ningún rostro'}, 400

        rostro_nuevo = encodings[0]

        # 5) Obtener embeddings en memoria
        embeddings = obtener_embeddings_en_memoria()
        # [(usuario_id, np.ndarray), …]

        # 6) Comparar contra cada embedding
        for usuario_id, vector_guardado in embeddings:
            distancia = np.linalg.norm(vector_guardado - rostro_nuevo)
            if distancia < 0.6:
                usuario = Usuario.query.get(usuario_id)
                if not usuario:
                    continue

                # 7a) Coincidencia: emitir token
                payload = {
                    'user_id': usuario.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=3)
                }
                token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm='HS256')

                try:
                    with Image.open(usuario.imagen) as img:
                        orig_w, orig_h = img.size
                        new_h = 256
                        new_w = int(orig_w * new_h / orig_h)

                        # 1) Convertir a RGB y hacer resize usando LANCZOS
                        resample = Image.Resampling.LANCZOS if hasattr(Image, "Resampling") else Image.LANCZOS
                        thumb = img.convert("RGB").resize((new_w, new_h), resample)

                        # 2) Volcar a base64
                        buffer = io.BytesIO()
                        thumb.save(buffer, format="JPEG")
                        img_b64 = base64.b64encode(buffer.getvalue()).decode("ascii")
                        data_url = f"data:image/jpeg;base64,{img_b64}"
                except Exception as e:
                    log.error(f"Error procesando imagen del usuario: {e}", exc_info=True)
                    data_url = None

                return {
                    'mensaje': 'Autenticación exitosa',
                    'token': token,
                    'usuario': {
                        'id': usuario.id,
                        'nombre': usuario.nombre,
                        'email': usuario.email,
                        'imagen': usuario.imagen if usuario.imagen else None,
                    },
                    'foto_perfil': data_url
                }, 200

        # 7b) Ninguna coincidencia
        return {'mensaje': 'No se encontró coincidencia facial'}, 401

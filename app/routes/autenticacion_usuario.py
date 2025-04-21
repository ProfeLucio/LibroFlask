from flask import request
from flask_restful import Resource
import face_recognition
import numpy as np
import jwt
import datetime

from app.models.usuario import Usuario
from app.config.settings import db, SECRET_KEY

class AutenticacionUsuario(Resource):
    def post(self):
        if 'imagen' not in request.files:
            return {'mensaje': 'Imagen no enviada'}, 400

        imagen = request.files['imagen']
        imagen_np = face_recognition.load_image_file(imagen)
        caras_codificadas = face_recognition.face_encodings(imagen_np)

        if not caras_codificadas:
            return {'mensaje': 'No se detectó ningún rostro'}, 400

        rostro_usuario = caras_codificadas[0]

        usuarios = Usuario.query.all()
        for usuario in usuarios:
            if usuario.embedding is None:
                continue

            embedding_guardado = np.frombuffer(usuario.embedding, dtype=np.float64)
            distancia = np.linalg.norm(embedding_guardado - rostro_usuario)

            if distancia < 0.6:
                token = jwt.encode({
                    'user_id': usuario.id,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=3)
                }, SECRET_KEY, algorithm='HS256')

                return {
                    'mensaje': 'Autenticación exitosa',
                    'token': token,
                    'usuario': {
                        'id': usuario.id,
                        'nombre': usuario.nombre,
                        'correo': usuario.correo
                    }
                }, 200

        return {'mensaje': 'No se encontró coincidencia facial'}, 401

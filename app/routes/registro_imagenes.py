# app/routes/registro_imagenes.py

import os
from flask import request, current_app
from flask_restful import Resource
from werkzeug.utils import secure_filename

from app.models.usuario import Usuario
from app.models import db
from app.services.face_processing import generar_embedding
from app.services.embedding_storage import guardar_embedding

class RegistroImagenes(Resource):
    def post(self, id):
        usuario = Usuario.query.get(id)
        if not usuario:
            return {"error": "Usuario no encontrado"}, 404

        imagen = request.files.get("imagen")
        if not imagen:
            return {"error": "Debe subir imagen"}, 400

        # 1. Guardar la imagen en disco
        carpeta = current_app.config["UPLOAD_FOLDER"]
        os.makedirs(carpeta, exist_ok=True)
        nombre = secure_filename(imagen.filename)
        ruta = os.path.join(carpeta, f"{id}_{nombre}")
        imagen.save(ruta)

        # 2. Actualizar ruta en Usuario y commit parcial
        usuario.imagen = ruta
        db.session.commit()

        # 3. Generar embedding y guardarlo
        emb = generar_embedding(ruta)
        if emb is not None:
            guardar_embedding(usuario.id, emb, ruta)

        return {"message": "Imagen cargada y usuario actualizado", "path": ruta}, 200

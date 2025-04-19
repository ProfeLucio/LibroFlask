import os
from flask import request, jsonify, current_app
from flask_restful import Resource
from werkzeug.utils import secure_filename
from app.models import db, Usuario

class RegistroImagenes(Resource):
    def post(self, id):
        usuario = Usuario.query.get(id)
        if not usuario:
            return {"error": "Usuario no encontrado"}, 404

        imagen1 = request.files.get("imagen1")
        imagen2 = request.files.get("imagen2")
        imagen3 = request.files.get("imagen3")

        if not imagen1 or not imagen2 or not imagen3:
            return {"error": "Debe subir tres imágenes"}, 400

        def guardar(imagen, num):
            nombre_seguro = secure_filename(imagen.filename)
            ruta = os.path.join(current_app.config["UPLOAD_FOLDER"], f"{id}_{num}_{nombre_seguro}")
            imagen.save(ruta)
            return ruta

        usuario.imagen_1 = guardar(imagen1, 1)
        usuario.imagen_2 = guardar(imagen2, 2)
        usuario.imagen_3 = guardar(imagen3, 3)
        usuario.registrado_completo = True

        db.session.commit()
        return {"message": "Imágenes cargadas y usuario actualizado"}, 200

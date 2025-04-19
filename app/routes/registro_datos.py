from flask import request, jsonify
from flask_restful import Resource
from app.models import db, Usuario

class RegistroDatos(Resource):
    def post(self):
        datos = request.get_json()
        nombre = datos.get("nombre")
        correo = datos.get("correo")

        if not nombre or not correo:
            return {"error": "Nombre y correo son obligatorios"}, 400

        if Usuario.query.filter_by(correo=correo).first():
            return {"error": "El correo ya está registrado"}, 409

        usuario = Usuario(nombre=nombre, correo=correo)
        db.session.add(usuario)
        db.session.commit()

        return {"message": "Usuario registrado", "id": usuario.id}, 201

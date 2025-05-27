from flask import request, jsonify
from flask_restful import Resource
from app.models import db, Usuario

class RegistroDatos(Resource):
    def post(self):
        datos = request.get_json()
        nombre = datos.get("nombre")
        email = datos.get("email")

        if not nombre or not email:
            return {"error": "Nombre y email son obligatorios"}, 400

        if Usuario.query.filter_by(email=email).first():
            return {"error": "El email ya está registrado"}, 409

        usuario = Usuario(nombre=nombre, email=email)
        db.session.add(usuario)
        db.session.commit()

        return {"message": "Usuario registrado", "id": usuario.id}, 201

#Listar los usuarios registrados en la base de datos
from flask_restful import Resource,  reqparse
from flask import Blueprint, jsonify
from app.models.usuario import Usuario

class ListarUsuarios(Resource):
    def get(self):
        usuarios = Usuario.query.all()
        usuarios_data = []
        for usuario in usuarios:
            usuarios_data.append({
                'id': usuario.id,
                'nombre': usuario.nombre,
                'email': usuario.email
            })
        return jsonify(usuarios_data)   
    
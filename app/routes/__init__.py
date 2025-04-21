from flask import Blueprint
from flask_restful import Api

from .registro_datos import RegistroDatos
from .registro_imagenes import RegistroImagenes
from .autenticacion_usuario import AutenticacionUsuario
from .perfil_usuario import ActualizarPerfil

usuarios_bp = Blueprint("usuarios", __name__)
api = Api(usuarios_bp)

api.add_resource(RegistroDatos, "/registro-datos")
api.add_resource(RegistroImagenes, "/registro-imagenes/<string:id>")
api.add_resource(AutenticacionUsuario, "/autenticacion") 
api.add_resource(ActualizarPerfil, "/actualizar-perfil")

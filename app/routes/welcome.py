from flask import Blueprint, jsonify

welcome_bp = Blueprint("welcome", __name__)

@welcome_bp.route("/", methods=["GET"])
def welcome():
    return jsonify({
        "mensaje": "Bienvenido a la API de autenticación con Face Recognition y JWT",
    }), 200
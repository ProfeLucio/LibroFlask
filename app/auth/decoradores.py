# app/auth/decoradores.py

from functools import wraps
from flask import request, current_app, jsonify, g
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # 1. Obtener el token (puedes usar "Bearer <token>" o solo el token directamente)
        auth_header = request.headers.get('Authorization', None)
        if not auth_header:
            return jsonify({'mensaje': 'Token requerido'}), 403

        # Si viene como "Bearer <token>", separa:
        parts = auth_header.split()
        if parts[0].lower() == 'bearer' and len(parts) == 2:
            token = parts[1]
        else:
            token = auth_header

        # 2. Decodificar y validar
        try:
            secret = current_app.config["SECRET_KEY"]
            payload = jwt.decode(token, secret, algorithms=["HS256"])
            # 3. Inyectar user_id en flask.g
            g.user_id = payload.get('user_id')
            if g.user_id is None:
                return jsonify({'mensaje': 'Token inválido'}), 401
        except jwt.ExpiredSignatureError:
            return jsonify({'mensaje': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'mensaje': 'Token inválido'}), 401

        # 4. Llamar a la función original
        return f(*args, **kwargs)
    return decorated

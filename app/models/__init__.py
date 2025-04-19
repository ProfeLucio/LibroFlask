from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importar aquí para que esté disponible globalmente
from .usuario import Usuario

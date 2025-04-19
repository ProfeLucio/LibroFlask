from app.models import db
import uuid

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), unique=True, nullable=False)
    imagen_1 = db.Column(db.String(255), nullable=True)
    imagen_2 = db.Column(db.String(255), nullable=True)
    imagen_3 = db.Column(db.String(255), nullable=True)
    registrado_completo = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Usuario {self.nombre} ({self.correo})>"

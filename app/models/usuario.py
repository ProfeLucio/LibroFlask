from app.models import db
import uuid

class Usuario(db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    imagen = db.Column(db.String(100), nullable=True)


    def __repr__(self):
        return f"<Usuario {self.nombre} ({self.email})>"

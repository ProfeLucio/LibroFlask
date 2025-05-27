# app/models/embedding_facial.py

import uuid
from app.models import db

class EmbeddingFacial(db.Model):
    __tablename__ = "embeddings_faciales"

    id               = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    usuario_id       = db.Column(db.String, db.ForeignKey("usuarios.id"), nullable=False)
    vector           = db.Column(db.LargeBinary, nullable=False)
    imagen_original  = db.Column(db.String(100), nullable=True)

    # Relación inversa opcional
    usuario = db.relationship("Usuario", backref="embeddings_faciales")

    def __repr__(self):
        return f"<EmbeddingFacial usuario_id={self.usuario_id}>"

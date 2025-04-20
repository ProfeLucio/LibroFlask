from app.models import db
import uuid

class EmbeddingFacial(db.Model):
    __tablename__ = "embeddings_faciales"

    id = db.Column(db.String, primary_key=True, default=lambda: str(uuid.uuid4()))
    usuario_id = db.Column(db.String, db.ForeignKey("usuarios.id"), nullable=False)
    vector = db.Column(db.LargeBinary, nullable=False)
    imagen_original = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"<Embedding usuario_id={self.usuario_id}>"

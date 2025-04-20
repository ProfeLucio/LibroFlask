from app.models import db, EmbeddingFacial
import numpy as np

def guardar_embedding(usuario_id, vector, ruta_imagen=None):
    vector_bytes = vector.tobytes()
    embedding = EmbeddingFacial(
        usuario_id=usuario_id,
        vector=vector_bytes,
        imagen_original=ruta_imagen
    )
    db.session.add(embedding)
    db.session.commit()

from app.models import EmbeddingFacial
import numpy as np

def obtener_embeddings_en_memoria():
    registros = EmbeddingFacial.query.all()
    return [
        (e.usuario_id, np.frombuffer(e.vector, dtype=np.float64))
        for e in registros
    ]

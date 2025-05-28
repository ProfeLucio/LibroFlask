# app/services/face_processing.py

import face_recognition
import numpy as np
from PIL import Image
import logging

log = logging.getLogger(__name__)

def generar_embedding(ruta_imagen: str):
    """
    Carga la imagen, la convierte a RGB|uint8 contiguo y extrae el embedding.
    Si no hay cara o falla, devuelve None.
    """
    try:
        # 1. Lee y convierte a RGB sin canal alfa
        with Image.open(ruta_imagen) as pil_img:
            pil_rgb = pil_img.convert("RGB")
            arr = np.asarray(pil_rgb, dtype=np.uint8)

        # 2. FORZAR memoria C-contigua (requisito de dlib)
        arr = np.ascontiguousarray(arr)

        #log.debug(f"generar_embedding: dtype={arr.dtype}, shape={arr.shape}, contig={arr.flags['C_CONTIGUOUS']}")

        # 3. Extrae embeddings
        encs = face_recognition.face_encodings(arr)
        return encs[0] if encs else None

    except Exception as e:
        log.warning(f"Error generando embedding: {e}", exc_info=True)
        return None

import face_recognition

def generar_embedding(ruta_imagen):
    imagen = face_recognition.load_image_file(ruta_imagen)
    encodings = face_recognition.face_encodings(imagen)
    if encodings:
        return encodings[0]
    return None


# 🔐 API REST de Reconocimiento Facial con Flask

Este proyecto corresponde a la **rama `main`** de una API REST construida con **Flask**, orientada al registro y autenticación de usuarios mediante **reconocimiento facial**. Integra tecnologías modernas como:

- Procesamiento de imágenes con `face_recognition` y `OpenCV`
- Generación y comparación de *embeddings* faciales
- Autenticación biométrica con generación de **JWT**
- Estructura modular usando `Flask-RESTful`
- Almacenamiento en base de datos SQLite con `SQLAlchemy`

## 🧠 ¿Qué hace esta API?
Permite registrar usuarios en dos pasos:
1. Enviar nombre y correo.
2. Tomar tres fotografías del rostro, procesarlas y generar un *embedding* único.

Luego, el usuario puede iniciar sesión enviando una nueva imagen facial, que será comparada contra la base de datos. Si hay coincidencia, se le otorgará un **token JWT** con el que podrá acceder a rutas protegidas, como actualizar su perfil.

---

## 📁 Estructura de Directorios

```
flask_api/
├── app/
│   ├── auth/                    # Decoradores personalizados, como @token_required
│   │   └── decoradores.py
│   ├── config/                  # Configuración global (SECRET_KEY, DB, etc.)
│   │   └── settings.py
│   ├── models/                  # Modelos SQLAlchemy: Usuario, Embedding
│   │   ├── embedding.py
│   │   └── usuario.py
│   ├── routes/                  # Recursos de la API RESTful
│   │   ├── autenticacion_usuario.py
│   │   ├── perfil_usuario.py
│   │   ├── registro_datos.py
│   │   ├── registro_imagenes.py
│   │   └── __init__.py
│   └── services/                # Lógica de negocio: embeddings, procesamiento facial
│       ├── embedding_query.py
│       ├── embedding_storage.py
│       └── face_processing.py
├── model_faces/                 # Almacena la base de datos SQLite
├── uploads/                     # Carpeta donde se guardan las imágenes subidas
├── requirements.txt             # Dependencias del proyecto
├── server.py                    # Punto de entrada principal del backend
└── README.md                    # Documentación del proyecto
```

---

## 🚀 Cómo iniciar el servidor

1. Instala las dependencias:
```bash
pip install -r requirements.txt
```

2. Ejecuta el servidor Flask:
```bash
python server.py
```

El backend quedará disponible en `http://localhost:5000`

---

## 📌 Rutas principales

- `POST /registro-datos` – Guarda nombre y correo del usuario.
- `POST /registro-imagenes/<id>` – Procesa las imágenes y genera el embedding facial.
- `POST /autenticacion` – Recibe una imagen y autentica al usuario.
- `PUT /actualizar-perfil` – Requiere token JWT, permite actualizar nombre y correo.

---

## 🔒 Seguridad y JWT

Las rutas protegidas requieren el envío de un token JWT válido en la cabecera:
```
Authorization: <token_jwt>
```

---

## 👨‍💻 Autor
+
Gonzalo Andrés Lucio López  
[[Linkedin]](www.linkedin.com/in/glucio/)  
[[GitHub]](https://github.com/ProfeLucio)  
[[Youtube]](https://www.youtube.com/@ProfeLucio) 
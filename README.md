
# 📂 Proyecto Flask API - Registro de Usuarios con Imágenes

Este proyecto en Flask implementa el flujo inicial para el **registro de usuarios** en dos etapas:

1. Registro de los datos básicos del usuario.
2. Subida de tres imágenes faciales asociadas al usuario.

> **Nota:** Esta versión documenta únicamente el flujo de captura inicial. La lógica de reconocimiento facial y embeddings se desarrollará en una etapa posterior.

## 📁 Estructura del Proyecto

```
flask_api/
├── app/
│   ├── config/
│   │   └── settings.py           # Configuración de base de datos y carpeta de subida
│   ├── models/
│   │   ├── __init__.py           # Inicialización de SQLAlchemy
│   │   ├── usuario.py            # Modelo de Usuario con datos y campos de imagen
│   │   └── embedding.py          # Modelo de embeddings faciales asociados al usuario
│   ├── routes/
│   │   ├── __init__.py           # Registro de rutas con Blueprint
│   │   ├── registro_datos.py     # Paso 1: registro de nombre y correo
│   │   └── registro_imagenes.py  # Paso 2: subida de imágenes del rostro
│   ├── services/                 # Servicios auxiliares del sistema
│   │   ├── embedding_query.py
│   │   ├── embedding_storage.py
│   │   └── face_processing.py
├── uploads/                      # Carpeta donde se almacenan las imágenes subidas
├── server.py                     # Punto de entrada principal de la aplicación
├── requirements.txt              # Lista de dependencias del entorno
└── README.md                     # Documentación del proyecto
```

## 🚀 Flujo de Registro de Usuario

### 1. `POST /usuarios/registro-datos`

Registra un usuario con su nombre y correo electrónico.

**Entrada esperada (JSON):**
```json
{
  "nombre": "Juan Pérez",
  "correo": "juan@example.com"
}
```

**Respuesta exitosa:**
```json
{
  "message": "Usuario registrado",
  "id": "UUID-del-usuario"
}
```

### 2. `POST /usuarios/registro-imagenes/<id>`

Permite subir tres imágenes del rostro del usuario previamente registrado.

**Entrada esperada (form-data):**
- imagen1: archivo
- imagen2: archivo
- imagen3: archivo

**Respuesta exitosa:**
```json
{
  "message": "Imágenes cargadas y usuario actualizado"
}
```

## 🧱 Requisitos del sistema

- Python 3.8 o superior
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- Werkzeug

## 📦 Instalación rápida

1. Clona el repositorio y entra en la carpeta del proyecto:

```bash
git clone https://github.com/tu_usuario/flask_api.git
cd flask_api
```

2. Instala las dependencias:

```bash
pip install -r requirements.txt
```

3. Inicia el servidor:

```bash
python server.py
```
# Estructura Base del Proyecto Flask - Reconocimiento Facial

Este branch representa la **versión inicial** del proyecto, con la estructura de carpetas organizada y los archivos fundamentales listos para comenzar el desarrollo de una API Flask centrada en autenticación mediante reconocimiento facial.

> ⚠️ **Importante:** Este branch NO contiene la implementación completa. Solo define la estructura y archivos base. La rama principal será `main` una vez finalizado el desarrollo.

---

## 📂 Estructura del Proyecto

```bash
flask_api/
├── .gitignore                 # Archivos y carpetas excluidos del control de versiones
├── requirements.txt           # Dependencias necesarias del entorno
├── README.md                  # Este documento
├── uploads/                   # Carpeta donde se almacenarán las imágenes faciales
├── model_faces/               # Carpeta reservada para modelos faciales (embeddings, etc.)
└── app/    
    ├── models/                # Definición de modelos SQLAlchemy
    ├── routes/                # Endpoints y controladores API REST
    ├── services/              # Lógica de negocio (procesamiento facial, etc.)
    └── config/                # Configuración de la aplicación
    
# Requisitos Iniciales
Antes de ejecutar la aplicación, asegúrate de tener instalado:

Python 3.8+

pip

Un entorno virtual (recomendado)

# Clonar el repositorio
git clone <url-del-repo>
cd flask_api

# Cambiar a la rama inicial
git checkout estructura-inicial

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows

# Instalar dependencias
pip install -r requirements.txt

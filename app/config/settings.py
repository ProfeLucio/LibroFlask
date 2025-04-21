import os
class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///auth.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
    SECRET_KEY = os.environ.get('SECRET_KEY', 'libroFlaskSecret')
    
from flask import Flask
from flask_cors import CORS
from app.models import db
from app.routes import usuarios_bp, welcome_bp
from app.config.settings import Config

app = Flask(__name__)
app.config.from_object(Config)

CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

db.init_app(app)
app.register_blueprint(welcome_bp)       
app.register_blueprint(usuarios_bp, url_prefix="/usuarios")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

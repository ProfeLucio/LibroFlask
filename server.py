from flask import Flask
from app.models import db
from app.routes import usuarios_bp
from app.config.settings import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(usuarios_bp, url_prefix="/usuarios")

if __name__ == "__main__":
    app.run(debug=True)

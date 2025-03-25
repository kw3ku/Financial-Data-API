from flask import Flask
from app.config import Config
from app.extensions import db, bcrypt, jwt
from app.routes import api_blueprint
from app.auth import auth_bp
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register blueprints
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/auth')

    with app.app_context():
        db.create_all()  # Ensure tables exist

    return app

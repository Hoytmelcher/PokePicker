from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    login.login_view='/login'
    login.login_message="Make sure you log in"

    from app.blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.blueprints.user import bp as social_bp
    app.register_blueprint(social_bp)

    from app.blueprints.api import bp as api_bp
    app.register_blueprint(api_bp)

    from app.blueprints.pokemon import bp as poke_bp
    app.register_blueprint(poke_bp)

    return app
   
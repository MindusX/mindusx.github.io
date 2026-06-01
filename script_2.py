from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
csrf = CSRFProtect()


def create_app(config_class=None):
    app = Flask(__name__)
    app.config.from_object(config_class or 'app.config.DevelopmentConfig')

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # blueprints
    from .routes.auth import auth_bp
    from .routes.sms import sms_bp
    from .routes.api import api_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(sms_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
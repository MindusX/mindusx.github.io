# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()          # protection CSRF automatique

def create_app():
    """Application factory"""
    app = Flask(__name__, instance_relative_config=False)

    # ------------------------------------------------------------------
    # Configuration    # ------------------------------------------------------------------
    app.config.from_mapping(
        SECRET_KEY="dev",                     # à changer en prod
        SQLALCHEMY_DATABASE_URI="sqlite:///data.db",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        WTF_CSRF_ENABLED=True,
        TEMPLATES_AUTO_RELOAD=True,
    )

    # ------------------------------------------------------------------
    # Initialisation des extensions
    # ------------------------------------------------------------------
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # ------------------------------------------------------------------
    # Enregistrement des blueprints (routes)
    # ------------------------------------------------------------------
    from .routes import main_bp
    app.register_blueprint(main_bp)

    # ------------------------------------------------------------------
    # Création de la base de données si elle n’existe pas
    # ------------------------------------------------------------------
    @app.before_first_request
    def create_tables():
        db.create_all()

    return app
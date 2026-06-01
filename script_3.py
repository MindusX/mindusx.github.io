import os


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql+psycopg2://postgres:postgres@db:5432/smsdb'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_FROM_NUMBER = os.getenv('TWILIO_FROM_NUMBER')
    # Flask-Login
    LOGIN_VIEW = 'auth.login'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV = 'development'


class ProductionConfig(BaseConfig):
    DEBUG = False
    ENV = 'production'
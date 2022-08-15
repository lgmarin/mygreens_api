import os

class Config:
    TESTING = os.environ.get("APP_ENV", "False")
    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecret")
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'

class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True

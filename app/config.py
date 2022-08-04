import os

class Config:
    TESTING = os.environ.get("APP_ENV", "False")
    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecret")

class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    TESTING = True

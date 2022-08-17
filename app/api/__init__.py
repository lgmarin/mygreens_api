from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import configs
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(configs[config_name])

    db.init_app(app)

    from .controllers import products
    app.register_blueprint(products, url_prefix="")

    return app

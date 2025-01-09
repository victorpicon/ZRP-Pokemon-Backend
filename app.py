from flask import Flask
from flask_smorest import Api

import db


def create_app():
    app = Flask(__name__)

    app.config["API_TITLE"] = "Pokedex Abilities REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/docs"
    app.config["OPENAPI_SWAGGER_UI_URL"] = (
        "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    )
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///pokemon.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    db.init_app(app)
    # api = Api(app)

    with app.app_context():
        db.create_all()

    return app
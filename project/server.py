import logging

from flask import Flask, jsonify
from flask_cors import CORS

from project.config import get_config
from project.exceptions import BaseServiceError
from project.setup.api import api
from project.setup.db import db
from project.views import auth_ns, genres_ns, user_ns, movies_ns, director_ns


def base_service_error_handler(exception: BaseServiceError):
    return jsonify({'error': str(exception)}), exception.code


def create_app(config_obj: str) -> Flask:
    app = Flask(__name__)
    app.config.from_object(get_config(config_obj))
    app.logger.setLevel(logging.DEBUG if app.config["DEBUG"] else logging.INFO)

    CORS(app=app)
    db.init_app(app)
    api.init_app(app)

    # Регистрация эндпоинтов
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(director_ns)

    app.register_error_handler(BaseServiceError, base_service_error_handler)

    @app.route('/ping/')
    def health_check():
        return jsonify({'status': 'ok'})

    return app

from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from views.auth import auth_ns
from views.user import user_ns
from implemented import user_service


def create_app(config_object):
    """ создаем приложение Flask, импортируем конфигурацию"""
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    """ создаем Api и подключение к БД"""
    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)
    create_data(app, db)


def create_data(app, db):
    """ наполняем БД тестовыми пользователями """
    with app.app_context():
        db.create_all()

        u1 = {"username": "vasya", "password": "my_little_pony", "role": "user"}
        u2 = {"username": "oleg", "password": "qwerty", "role": "user"}
        u3 = {"username": "oleg", "password": "P@ssw0rd", "role": "admin"}

        users = [u1, u2]

        for user in users:
            user_service.create(user)


app = create_app(Config())


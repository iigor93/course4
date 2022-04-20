""" Создание нового пользователя"""


from flask_restx import Resource, Namespace
from flask import request, abort
from implemented import user_service
from service.decorators import admin_required
from dao.model.user import UserSchema


user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    def get(self):
        rs = user_service.get_all()
        res = UserSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        data = request.json
        if 'username' in data and 'password' in data and 'role' in data:
            user_service.create(data)
            return "", 201
        return 400

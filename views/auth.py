from flask_restx import Resource, Namespace
from flask import request, abort
from implemented import auth_service


auth_ns = Namespace('auth')


@auth_ns.route('/')
class AuthView(Resource):
    def post(self):
        """ получение access_token и refresh_token по логину и паролю"""
        data = request.json
        if 'username' in data and 'password' in data:
            tokens = auth_service.check_user(data)
            if tokens:
                return tokens
        return abort(401)

    def put(self):
        """ получение новых токенов по refresh token"""
        data = request.json
        if 'refresh_token' in data:
            tokens = auth_service.refresh_tokens(data)
            if tokens:
                return tokens
        return abort(401)

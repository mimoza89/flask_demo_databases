from flask_restful import Resource
from flask import request

from managers.auth import AuthManager
from utils.decorators import validate_schema
from schemas.request_schemas.users import UserRegisterRequestSchema


class RegisterResource(Resource):
    @validate_schema(UserRegisterRequestSchema)
    def post(self):
        data = request.get_json()
        user = AuthManager.create_user(data)
        return AuthManager.encode_token(user)


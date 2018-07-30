from flask import request, jsonify, Blueprint
from flask.views import MethodView
from app.validate import FieldValidation

validate = FieldValidation()
auth_blueprint = Blueprint("auth_blueprint", __name__)

class RegisterUser(MethodView):
    """ class to register a user """

    def post(self):
        """Create a new user"""
        pass
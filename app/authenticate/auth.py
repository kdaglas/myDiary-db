from flask import request, jsonify, Blueprint
from flask.views import MethodView
from app.validate import FieldValidation
from app.database.dbfuncs import add_new_user, get_user_by_username
from app.models import User
from flask_jwt_extended import create_access_token

validate = FieldValidation()
auth_blueprint = Blueprint("auth_blueprint", __name__)


class RegisterUser(MethodView):
    """ class to register a diary user"""

    def post(self):
        """Create a new user"""
        reg_info = request.get_json()

        username = reg_info.get("username")
        emailaddress = reg_info.get("emailaddress")
        password = reg_info.get("password")

        response = validate.user_validation(username, emailaddress, password)

        if response:
            return response

        # a function that adds new user to the database
        add_new_user(
            username=username,
            emailaddress=emailaddress,
            password=password
        )

        new_user = User(
            username=username,
            emailaddress=emailaddress,
            password=password
        )
        return jsonify({"New user": new_user.__dict__}), 200


class Login(MethodView):
    """ class showing login for a user """

    def post(self):
        """ user login """

        request_data = request.get_json()
        username = request_data.get('username')
        password = request_data.get('password')

        response = validate.login_validation(username, password)

        if response:
            return response

        user_token = {}
        user = get_user_by_username(username)

        if user:

            access_token = create_access_token(identity=username)
            user_token["token"] = access_token
            return jsonify(user_token), 200

        return response


login_view = Login.as_view('login_view')
registry_view = RegisterUser.as_view('registry_view')

auth_blueprint.add_url_rule('/api/v1/user/login',
                            view_func=login_view, methods=['POST'])
auth_blueprint.add_url_rule("/api/v1/user/register",
                            view_func=registry_view, methods=['POST'])

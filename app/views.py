from flask import jsonify, request, Blueprint
from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.validate import FieldValidation


validate = FieldValidation()
_blueprint = Blueprint()
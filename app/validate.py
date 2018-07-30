"""validating user input fields"""
from flask import jsonify


class FieldValidation:

    def client_validation(self, username, emailaddress, password):

        if not username:
            return jsonify({"message": "username is missing"}), 400
        if not password:
            return jsonify({"message": "password is missing"}), 400
        if not emailaddress:
            return jsonify({"message": "emailaddress is missing"}), 400
        

    def validate_entered_id(self, id):
        pass

   

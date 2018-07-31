""" This file is for validating user input fields"""
from flask import jsonify


class FieldValidation:

    def user_validation(self, username, emailadress, password):

        if not username:
            return jsonify({"message": "username is missing"}), 400
        if not emailaddress:
            return jsonify({"message": "emailaddress is missing"}), 400
        if not password:
            return jsonify({"message": "password is missing"}), 400


    def login_validation(self, username, password):
        if not username:
            return jsonify({"message": "missing or wrong username"}), 400
        if not password:
            return jsonify({"message": "missing or wrong password"}), 400

    def entry_validation(self, title, content):

        if not title:
            return jsonify({"message": "the title is missing"}), 400
        if not content:
            return jsonify({"message": "the content is missing"}), 400


    # def validate_entered_id(self, id):
    #     try:
    #         entry_id = int(id)
    #     except ValueError:
    #         return jsonify({"message": "id should be an interger"}), 400


   

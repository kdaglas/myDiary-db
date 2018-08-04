from flask import jsonify, request
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from app import app
import re
from functools import wraps
from app.database.dbfuncs import add_new_user, get_user_by_username, add_new_entry, get_all_entries, get_single_entry, delete_single_entry, get_user_by_id, get_entry_by_id, update_single_entry
from app.models import User, DiaryEntry
from datetime import date


@app.route("/api/v1/login", methods=['POST'])
def login():

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username:
        return jsonify({"message": "Missing username parameter"}), 400
    elif not re.search("^[a-zA-Z]", username):
        return jsonify({"message": "username should be characters"}), 400
    if not password:
        return jsonify({"message": "Missing password parameter"}), 400
    elif not re.search(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{7,}$", password):
        return jsonify({"message": "Password should be 7 characters, 1 letter, 1 number"}), 400

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route("/api/v1/register", methods=['POST'])
def register():

    data = request.get_json()
    username = data.get('username')
    emailaddress = data.get('emailaddress')
    password = data.get('password')

    if not username:
        return jsonify({"message": "Missing username parameter"}), 400
    elif not re.search("^[a-zA-Z]", username):
        return jsonify({"message": "username should be characters"}), 400
    if not emailaddress:
        return jsonify({"message": "emailaddress is missing"}), 400
    elif not re.search(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", emailaddress):
        return jsonify({"message": "Email address in wrong format"}), 400
    if not password:
        return jsonify({"message": "Missing password parameter"}), 400
<<<<<<< HEAD
    elif not re.search("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{7,}$", password):
=======
    elif not re.search(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{7,}$", password):
>>>>>>> 227183d708bf02fa23a64c9bfad9ee25371febe0
        return jsonify({"message": "password must have 7 characters, 1 letter and 1 number"}), 400

    add_new_user(username, emailaddress, password)

    return jsonify({'message': 'Successfully signed up'}), 200


@app.route("/api/v1/diaries", methods=['POST'])
@jwt_required
def add_entry():
    data = request.get_json()
    day = date.today()
    title = data.get('title')
    content = data.get('content')

    if not title:
        return jsonify({"message": "Title is missing"}), 400
    elif not re.search("^[a-zA-Z]", title):
        return jsonify({"message": "title should be characters"}), 400
    if not content:
        return jsonify({"message": "content is missing"}), 400

    add_new_entry(day, title, content)

    return jsonify({'message': 'Entry successfully added'}), 200


@app.route("/api/v1/diaries", methods=['GET'])
@jwt_required
def getAllEntries():

    all_entries = get_all_entries()
    lst = []
    for data in all_entries:
        dic = {}
        dic["entry_id"] = data[0]
        dic["day"] = data[1]
        dic["title"] = data[2]
        dic["content"] = data[3]
        lst.append(dic)

    return jsonify({'message': 'All entries successfully viewed',
                    'All_entries_here': lst}), 200


@app.route("/api/v1/diaries/<entry_id>", methods=["GET"])
@jwt_required
def getting_single_entry(entry_id):
    entry = get_single_entry(entry_id)

    if not entry:
        return jsonify({'message': 'No such entry made'})

    return jsonify({'message': 'Single entry successfully viewed',
                    'Single_entry_here': entry}), 200


@app.route('/api/v1/diaries/<entry_id>', methods=['PUT'])
@jwt_required
def edit_entry(entry_id):
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    if title or content:
        res = update_single_entry(entry_id, title, content)
        if res == "not found":
            return jsonify({"message": "Not found"}), 404
        else:
            return jsonify({"message": "Successfully edited"}), 201
    else:
        return jsonify({"message": "Either title or content is empty"})


@app.route("/api/v1/diaries/<entry_id>", methods=['DELETE'])
@jwt_required
def deleting_single_entries(entry_id):
    entry = {}
    entry = delete_single_entry(entry_id)

    return entry

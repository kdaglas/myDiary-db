from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from app.validate import FieldValidation
from app import app
from functools import wraps
from app.database.dbfuncs import add_new_user, get_user_by_username, add_new_entry, get_all_entries, get_single_entry, delete_single_entry, get_user_by_id, get_entry_by_id
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, DiaryEntry
from datetime import date


validate = FieldValidation()


@app.route("/api/v1/login", methods=['POST'])
def login():

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # cursor = connect.get_connection().cursor()

    # cursor.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(username, password))
    # rows = cursor.fetchone()
    # if not rows:
    #     return {"message": "User does not exist"}
    # return rows

    if not username:
        return jsonify({"message": "Missing username parameter"}), 400
    if not password:
        return jsonify({"message": "Missing password parameter"}), 400


    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route("/api/v1/register", methods=['POST'])
def register():

    data = request.get_json()
    username = data.get('username')
    emailaddress = data.get('emailaddress')
    password = data.get('password')

    add_new_user(username, emailaddress, password)

    return jsonify({'message': 'Successfully signed up'}), 200


@app.route("/api/v1/diaries", methods=['POST'])
@jwt_required
def add_entry(username):
    data = request.get_json()
    day = date.today()
    title = data.get('title')
    content = data.get('content')

    add_new_entry(day, title, content)

    return jsonify({'message': 'Entry successfully added'}), 200


@app.route("/api/v1/diaries", methods=['GET'])
@jwt_required
def getAllEntries(username):

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
def getting_single_entry(username, entry_id):
    entry = get_single_entry(entry_id)

    if not entry:
        return jsonify({'message': 'No such entry made'})

    data = request.get_json()
    dic = {}
    dic["entry_id"] = data[0]
    dic["day"] = data[1]
    dic["title"] = data[2]
    dic["content"] = data[3]

    return jsonify({'message': 'Single entry successfully viewed',
                    'Single_entry_here': dic}), 200


@app.route('/api/v1/diaries/<entry_id>', methods=['PUT'])
@jwt_required
def edit_entry(username, entry_id):
    data = request.get_json()
    new_entry = {}
    new_entry['title'] = data.get('title')
    new_entry['content'] = data.get('content')
    for entry in all_entries:
        if entry.id == int(entry_id):
            entry.title = new_entry['title']
            entry.content = new_entry['content']
            return jsonify({"message": "Entry has been modified"}), 200
        return jsonify({"message": "No such entry"}), 404
    return jsonify({"message": "Single entry id has to be bigger than zero"}), 404


@app.route("/api/v1/diaries/<entry_id>", methods=['DELETE'])
@jwt_required
def deleting_single_entries(username, entry_id):
    entry = {}
    entry = delete_single_entry(entry_id)

    if not entry:
        return jsonify({'message': 'No such entry made'})

    if type(DiaryEntry.get_entry_by_id(user_id, entry_id)) == dict:
        return jsonify({entry.delete_single_entry(user_id, entry_id)}), 200
    return jsonify({'message': 'Single entry successfully deleted'}), 200

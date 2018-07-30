from app import app
import json
from flask import request, json, jsonify
from app.models import User, DiaryEntry
from datetime import date


Users = []
all_entries = []


@app.route("/api/v1/register", methods=['POST'])
def register():
    data = request.get_json()
    id = len(Users) + 1
    username = data.get('username')
    emailaddress = data.get('emailaddress')
    password = data.get('password')

    if len(username) < 1:
        return jsonify({'message': 'Username is missing'}), 400
    if len(emailaddress) < 1:
        return jsonify({'message': 'Emailaddress is missing'}), 400
    if len(password) < 1:
        return jsonify({'message': 'Password is missing'}), 400

    new_user = User(id, username, emailaddress, password)
    Users.append(new_user)
    return jsonify({'message': 'Diary successfully created'})


@app.route("/api/v1/login", methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if len(username) < 1:
        return jsonify({'message': 'Username is wrong'}), 400
    if len(password) < 1:
        return jsonify({'message': 'Password is wrong'}), 400

    return jsonify({'message': 'Successfully logged in'})


@app.route("/api/v1/diaries", methods=['POST'])
def add_entry():
    data = request.get_json()
    id = len(all_entries) + 1
    today = str(date.today())
    title = data.get('title')
    content = data.get('content')

    if len(title) < 1:
        return jsonify({'message': 'Title is missing'}), 400
    elif len(content) < 1:
        return jsonify({'message': 'Missing entry'}), 400

    for entry in all_entries:
        if entry.title == title:
            return jsonify({'message':'Same title made'})
    
    for entry in all_entries:
        if entry.content == content:
            return jsonify({'message':'Same content made'})
        
    new_entry = DiaryEntry(id, today, title, content)
    all_entries.append(new_entry)   
    
    return jsonify({'message': 'Entry successfully added'}), 200


@app.route("/api/v1/diaries", methods=['GET'])
def get_all_entries():
    if len(all_entries) > 0:
        print(all_entries)
        return jsonify({'message': 'All entries successfully viewed',
                        'All entries here': [
                            entry.__dict__ for entry in all_entries
                        ]}), 200

    return jsonify({'message': 'No entry added'}), 404


@app.route("/api/v1/diaries/<entry_id>", methods=["GET"])
def get_single_entry(entry_id):
    if int(entry_id) > 0:
        if len(all_entries) > 0:
            for entry in all_entries:
                if entry.id == int(entry_id):
                    return jsonify({
                        "message": "Single entry successfully viewed",
                        "Diary Entry": entry.__dict__
                    }), 200

            return jsonify({"message": "Entry doesnot exist"})
        return jsonify({"message": "No entry has been registered yet"}), 404
    return jsonify({"message": "Single entry id has to bigger than zero"}), 404


@app.route("/api/v1/diaries/<entry_id>", methods=["PUT"])
def edit_entry(entry_id):
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

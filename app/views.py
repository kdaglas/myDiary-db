from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from app.validate import FieldValidation
from app import app
from functools import wraps
# import jwt
from app.database.dbfuncs import add_new_user, get_user_by_username, add_new_entry, get_all_entries, get_single_entry, delete_single_entry, get_user_by_id
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, DiaryEntry
from datetime import date


validate = FieldValidation()
diary_blueprint = Blueprint("diary_blueprint", __name__)


# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = None

#         if 'token' in request.headers:
#             token = request.headers['token']
#         elif not token:
#             return jsonify({'token': 'token is missing'}), 401
#         try:
#             user_id = jwt.decode(token, config.JWT_SECRET_KEY)
#             current_user = get_user_by_id(user_id['id'])
#         except:
#             return jsonify({'message' : 'Token is no longer available!'}), 401
#         return f(current_user['user_id'], *args, **kwargs)
#     return decorated


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
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if username != 'test' or password != 'test':
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route("/api/v1/register", methods=['POST'])
@jwt_required
def register():

    data = request.get_json()
    username = data.get('username')
    emailaddress = data.get('emailaddress')
    password = data.get('password')

    add_new_user(username, emailaddress, password)

    return jsonify({'message': 'Successfully signed up'}), 200

    # new_user = User(data['username'], data['emailaddress'], data['password'])
    # result = add_new_user(new_user.username,new_user.emailaddress,new_user.password)
    # return str({
    #     "user_id": result[0],
    #     "username": result[1],
    #     "emailaddress": result[2],
    #     "password": result[3]
    # }), 200
    # return jsonify({'message': 'Successfully logged in'}), 200

    # pass
    # hashed_password = generate_password_hash(data['password'], method='sha256')
    # data = request.get_json()
    # username = data.get('username')
    # emailaddress = data.get('emailaddress')
    # password = data.get('password')

    # if len(username) < 1:
    #     return jsonify({'message': 'Username is missing'}), 400
    # if len(emailaddress) < 1:
    #     return jsonify({'message': 'Emailaddress is missing'}), 400
    # if len(password) < 1:
    #     return jsonify({'message': 'Password is missing'}), 400

    #
    # Users.append(new_user)
    # return jsonify({'message': 'Diary successfully created'})



    # data = request.get_json()
    # username = data.get('username')
    # password = data.get('password')

    # get_user_by_username(username, password)

    # return jsonify({'message': 'Successfully signed up'}), 200

    # if len(username) < 1:
    #     return jsonify({'message': 'Username is wrong'}), 400
    # if len(password) < 1:
    #     return jsonify({'message': 'Password is wrong'}), 400

    # return jsonify({'message': 'Successfully logged in'})


@app.route("/api/v1/diaries", methods=['POST'])
@jwt_required
def add_entry():
    data = request.get_json()
    day = date.today()
    title = data.get('title')
    content = data.get('content')

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
        dic["date"] = data[1]
        dic["title"] = data[2]
        dic["content"] = data[3]
        lst.append(dic)

    return jsonify({'message': 'All entries successfully viewed',
                    'All entries here': lst}), 200

    # all_entries = get_all_entries()
    # output = []
    # for entry in all_entries:
    #     entry_data = {}
    #     entry_data["entry_id"] = entry.entry_id
    #     entry_data["day"] = entry.day
    #     entry_data["title"] = entry.title
    #     entry_data["content"] = entry.content
    #     output.append(entry_data)

    # return jsonify({'message': 'All entries successfully viewed',
    #                 'All entries here': output}), 200


@app.route("/api/v1/diaries/<entry_id>", methods=["GET"])
@jwt_required
def getting_single_entry(entry_id):
    entry = get_single_entry(entry_id)

    if not entry:
        return jsonify({'message': 'No such entry made'})

    entry_data = {}
    entry_data["entry_id"] = entry.entry_id
    entry_data["day"] = entry.day
    entry_data["title"] = entry.title
    entry_data["content"] = entry.content

    return jsonify({'message': 'Single entry successfully viewed',
                    'Single entry here': entry_data}), 200

    # return jsonify({'message': 'Single entry successfully viewed',
    #                 'All entries here': entry}), 200


# @app.route("/api/v1/diaries/<entry_id>", methods=["PUT"])
# def edit_entry(entry_id):
#     data = request.get_json()
#     new_entry = {}
#     new_entry['title'] = data.get('title')
#     new_entry['content'] = data.get('content')

#     for entry in all_entries:
#         if entry.id == int(entry_id):
#             entry.title = new_entry['title']
#             entry.content = new_entry['content']
#             return jsonify({"message": "Entry has been modified"}), 200
#         return jsonify({"message": "No such entry"}), 404
#     return jsonify({"message": "Single entry id has to be bigger than zero"}), 404

@app.route("/api/v1/diaries/<entry_id>", methods=['DELETE'])
@jwt_required
def deleting_single_entries(entry_id):
    entry = {}
    entry = delete_single_entry(entry_id)

    # if not entry:
    #     return jsonify({'message': 'No such entry made'})

    # entry_data = {}
    # entry_data["entry_id"] = entry.entry_id
    # entry_data["day"] = entry.day
    # entry_data["title"] = entry.title
    # entry_data["content"] = entry.content

    return jsonify({'message': 'Single entry successfully deleted'}), 200

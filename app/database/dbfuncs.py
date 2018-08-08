""" Interaction with the db"""
from app.database.dbController import DatabaseConnection
from flask import jsonify
import psycopg2.extras

connect = DatabaseConnection()
cursor = connect.get_connection().cursor()


def add_new_user(username, emailaddress, password):
    query = (
        """INSERT INTO users (user_id, username, emailaddress, password)
         VALUES (DEFAULT, '{}', '{}', '{}')
         RETURNING user_id, username, emailaddress, password""".
        format(username, emailaddress, password))
    cursor.execute(query)
    rows = cursor.fetchone()
    return rows


def get_user_by_id(user_id):
    query = (
        """SELECT * from users where user_id = '{}'""".
        format(user_id))
    cursor.execute(query)
    rows = cursor.fetchone()
    return rows


def get_user_by_username(username):
    query = (
        """SELECT * from users where username = '{}'""".
        format(username))
    cursor.execute(query)
    username = cursor.fetchone()
    return username


def add_new_entry(day, title, content):
    query = (
        """INSERT INTO entries (entry_id, day, title, content) VALUES (DEFAULT,
            '{}', '{}', '{}')""".
        format(day, title, content))
    cursor.execute(query)


def get_entry_by_id(entry_id):
    query = (
        """SELECT * from entries where entry_id = '{}'""".
        format(entry_id))
    cursor.execute(query)
    rows = cursor.fetchone()
    return rows


def get_all_entries():
    cursor.execute("SELECT * FROM entries")
    all_entries = cursor.fetchall()
    return all_entries


def get_single_entry(entry_id):
    cursor = connect.get_connection().cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cursor.execute("SELECT * FROM entries WHERE entry_id = '{}'".
                   format(entry_id))
    rows = cursor.fetchone()
    if not rows:
        return {"message": "Entry does not exist"}
    return rows


# def update_single_entry(entry_id, title, content):
#     if get_single_entry(entry_id)["message"] == "Entry does not exist":
#         return "not found"
#     else:
#         cursor.execute("UPDATE entries SET title = %s, content = %s WHERE entry_id = %s",
#                         (title, content, entry_id))
#         return 'Entry edited'


def update_single_entry(entry_id):
    cursor.execute("UPDATE entries SET title = %s, content = %s WHERE entry_id = %s".
                   format(entry_id))
    rows = cursor.fetchone()
    if not rows:
        return {"message": "Entry does not exist"}
    return rows


def delete_single_entry(entry_id):
    cursor.execute("SELECT * FROM entries WHERE entry_id = '{}'".
                   format(entry_id))
    rows = cursor.fetchone()
    if rows:
        cursor.execute("DELETE FROM entries WHERE entry_id = '{}'".
                   format(entry_id))
        return jsonify({"message": "Entry successful deleted"})           
    else:
        return jsonify({"message": "Entry not found"})

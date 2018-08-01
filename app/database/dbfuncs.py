""" Interaction with the db"""
from app.database.dbController import DatabaseConnection

connect = DatabaseConnection()
cursor = connect.get_connection().cursor()


def add_new_user(username, emailaddress, password):
    query = (
        """INSERT INTO users (user_id, username, emailaddress, password) VALUES (DEFAULT, '{}', '{}', '{}') RETURNING user_id, username, emailaddress, password""".
        format(username, emailaddress, password))
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


def add_new_entry(entry_id, date, title, content):
    query = (
        """INSERT INTO entries (id, date, title, content) VALUES ('{}', '{}', '{}', '{}')""".
        format(entry_id, date, title, content))
    cursor.execute(query)


def get_all_entries():
    cursor.execute("SELECT * FROM entries")
    all_entries = cursor.fetchall()
    return all_entries
    

def get_single_entry(entry_id):
    cursor.execute("SELECT * FROM entries WHERE entry_id = '{}'".format(entry_id))
    rows = cursor.fetchone()
    if not rows:
        return {"message":"Entry does not exist"}
    return rows

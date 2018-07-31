""" Interaction with the db"""
from app.database.dbControl import DatabaseConnect

connect = DatabaseConnect()
cursor = connect.cursor


def add_new_user(username, emailaddress, password):
    query = (
        """INSERT INTO users (id,username, emailaddress, password) VALUES (DEFAULT, '{}', '{}', '{}')""".
        format(username, emailaddress, password))
    cursor.execute(query)


def get_user_by_username(username):
    query = (
        """SELECT * from users where username = '{}'""".
        format(username))
    cursor.execute(query)
    username = cursor.fetchone()
    return username
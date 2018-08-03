import unittest
from run import app
from flask import jsonify, json
from app.models import User
from app.database.dbController import DatabaseConnection


my_connection = DatabaseConnection()


class Test_auth(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config["TESTING"] = True
        # tear_down
        my_connection.delete_tables()
        my_connection.create_tables()

    def test_registering(self):
        """ Testing if user is successfully registered """
        response = self.app.post("/api/v1/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="Douglas", emailaddress="daglach7@gmail.com",
                                                      password="callmee"),)
                                 )
        self.assertEquals(response.status_code, 200)

    def test_registering_with_empty_username(self):
        """ Testing for empty username validation """
        response = self.app.post("/api/v1/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="", emailaddress="daglach7@gmail.com",
                                                      password="callmee"),)
                                 )
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Missing username parameter")
        self.assertEquals(response.status_code, 400)

    def test_registering_with_empty_emailaddress(self):
        """ Testing for empty emailaddress validation """
        response = self.app.post("/api/v1/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="Douglas", emailaddress="",
                                                      password="callmee"),)
                                 )
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "emailaddress is missing")
        self.assertEquals(response.status_code, 400)

    def test_registering_with_empty_password(self):
        """ Testing for empty password validation """
        response = self.app.post("/api/v1/register",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="Douglas", emailaddress="daglach7@gmail.com",
                                                      password=""),)
                                 )
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Missing password parameter")
        self.assertEquals(response.status_code, 400)

    def test_login_successful(self):
        """ Testing for successful login """
        response2 = self.app.post("/api/v1/register",
                                  content_type='application/json',
                                  data=json.dumps(dict(username="Douglas", emailaddress="daglach7@gmail.com",
                                                       password="callmee"),)
                                  )

        response = self.app.post("/api/v1/login",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="Douglas", password="callmee"))
                                 )
        reply = json.loads(response.data)
        self.assertEquals(response.status_code, 200)

    def test_login_with_wrong_or_no_username(self):
        """ Testing for wrong or no username credentials """
        response = self.app.post("/api/v1/login",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="", password="callmee"))
                                 )
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Missing username parameter")
        self.assertEquals(response.status_code, 400)

    def test_login_with_wrong_or_no_password(self):
        """ Testing for wrong or no password credentials """
        response = self.app.post("/api/v1/login",
                                 content_type='application/json',
                                 data=json.dumps(dict(username="Douglas", password=""))
                                 )
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Missing password parameter")
        self.assertEquals(response.status_code, 400)

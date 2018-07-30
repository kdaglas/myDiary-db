import unittest
from run import app
from flask import jsonify, json
from app.models import User

class Test_auth(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_registration(self):
        """ a test for successful user registration """
        response = self.app.post("/api/v1/register",
            content_type='application/json',
            data=json.dumps(dict(username="Douglas", emailaddress="daglach7@gmail.com", password="callmee"),)
            )      
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Diary successfully created")
        self.assertEquals(response.status_code, 200)

    
    def test_registration_with_empty_username(self):
        """ Test for empty username validation """
        response = self.app.post(
                "/api/v1/register",
            content_type='application/json',
            data=json.dumps(dict(username="", emailaddress="daglach7@gmail.com", password="callmee"),)
            )              
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Username is missing")
        self.assertEquals(response.status_code, 400)
      

    def test_registration_with_empty_emailaddress(self):
        """ Test for empty emailaddress validation """
        response = self.app.post("/api/v1/register",
            content_type='application/json',
            data=json.dumps(dict(username="Douglas", emailaddress="", password="callmee"),)
            )              
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Emailaddress is missing")
        self.assertEquals(response.status_code, 400)
    
    
    def test_registration_with_empty_password(self):
        """ Test for empty password validation """
        response = self.app.post("/api/v1/register",
            content_type='application/json',
            data=json.dumps(dict(username="Douglas", emailaddress="daglach7@gmail.com", password=""),)
            )              
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Password is missing")
        self.assertEquals(response.status_code, 400)

    
    def test_user_login_successful(self):
        """ Test for successful login """
        response = self.app.post("/api/v1/login",
            content_type='application/json',
            data=json.dumps(dict(username="Doug", password="callmee"))
            )            
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Successfully logged in")
        self.assertEquals(response.status_code, 200)


    def test_user_login_with_wrong_or_no_username(self):
        """ Test for login with wrong or no username """       
        response = self.app.post(
                "/api/v1/login",
                content_type='application/json',
                data=json.dumps(dict(username="", password="callmee"))
                )            
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Username is wrong")
        self.assertEquals(response.status_code, 400)


    def test_user_login_with_wrong_or_no_password(self):
        """ Test for login with wrong or no password """
        response = self.app.post(
                "/api/v1/login",
                content_type='application/json',
                data=json.dumps(dict(username="Doug", password=""))
                )            
        reply = json.loads(response.data)

        self.assertEquals(reply["message"], "Password is wrong")
        self.assertEquals(response.status_code, 400)

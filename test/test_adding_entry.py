import unittest
from run import app
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask import jsonify, json
from app.models import DiaryEntry
from app import views
from app.database.dbController import DatabaseConnection

my_connection = DatabaseConnection()


class Test_Diary_Entries(unittest.TestCase):

  def setUp(self):
    self.app = app.test_client()
    my_connection.delete_tables()
    my_connection.create_tables()

  def test_create_diary_entry(self):
    ''' Testing for diary entry creation '''

    response1 = self.app.post("/api/v1/register",
                              content_type='application/json',
                              data=json.dumps(dict(username="Douglas",
                                                   emailaddress="daglach7@gmail.com",
                                                   password="callmee"),)
                              )
    response = self.app.post("/api/v1/login",
                             content_type='application/json',
                             data=json.dumps(dict(username="Douglas",
                                                  password="callmee"))
                             )
    reply2 = json.loads(response.data.decode())

    response2 = self.app.post("/api/v1/diaries",
                              content_type='application/json', headers=dict(Authorization='Bearer ' + reply2['token']),
                              data=json.dumps(dict(title="Andela", content="The place for your coding skill level-up"),)
                              )
    self.assertEquals(response2.status_code, 201)

  def test_adding_entry_with_empty_title(self):
    """ Testing for empty title validation """

    response1 = self.app.post("/api/v1/register",
                              content_type='application/json',
                              data=json.dumps(dict(username="Douglas", emailaddress="daglach7@gmail.com",
                                                   password="callmee"),)
                              )
    response = self.app.post("/api/v1/login",
                             content_type='application/json',
                             data=json.dumps(dict(username="Douglas", password="callmee"))
                             )
    reply2 = json.loads(response.data.decode())

    response2 = self.app.post("/api/v1/diaries",
                              content_type='application/json', headers=dict(Authorization='Bearer ' + reply2['token']),
                              data=json.dumps(dict(title="", content="The place for your coding skill level-up"),)
                              )

    reply = json.loads(response2.data)
    self.assertEquals(reply.get("message"), "title is missing")
    self.assertEquals(response2.status_code, 400)

  def test_adding_entry_with_empty_content(self):
    """ Testing for empty content validation """

    response1 = self.app.post("/api/v1/register",
                              content_type='application/json',
                              data=json.dumps(dict(username="Douglas", emailaddress="daglach7@gmail.com",
                                                   password="callmee"),)
                              )
    response = self.app.post("/api/v1/login",
                             content_type='application/json',
                             data=json.dumps(dict(username="Douglas", password="callmee"))
                             )
    reply2 = json.loads(response.data.decode())

    response2 = self.app.post("/api/v1/diaries",
                              content_type='application/json', headers=dict(Authorization='Bearer ' + reply2['token']),
                              data=json.dumps(dict(title="Andela", content=""),)
                              )

    reply = json.loads(response2.data)
    self.assertEquals(reply.get("message"), "Content is missing")
    self.assertEquals(response2.status_code, 400)

import unittest
from run import app
from flask import jsonify, json
from app import views

class Test_Diary_Entries(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add_entry(self):
        """ a test for successful adding an entry """
        response = self.app.post("/api/v1/diaries", content_type='application/json',
                                data=json.dumps(dict(id="1", today="17.07.2018", title="Coding", content="The best way of life is code"),)
                                )      
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Entry successfully added")
        self.assertEquals(response.status_code, 200)

    
    def test_registration_with_empty_title(self):
        """ Test for empty title validation """
        response = self.app.post("/api/v1/diaries", content_type='application/json',
                                data=json.dumps(dict(id="1", today="17.07.2018", title="", content="The best way of life is code"),)
                                )              
        reply = json.loads(response.data)
        self.assertEquals(reply["message"], "Title is missing")
        self.assertEquals(response.status_code, 400)
      

    def test_registration_with_empty_content(self):
        """ Test for empty content validation """
        response = self.app.post("/api/v1/diaries", content_type='application/json',
                                data=json.dumps(dict(id="1", today="17.07.2018", title="Coding", content=""),)
                                )              
        reply = json.loads(response.data)
        self.assertEquals(reply['message'], 'Missing entry')
        self.assertEquals(response.status_code, 400)

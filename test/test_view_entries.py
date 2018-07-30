import unittest
from app import views
from run import app
import json

class Test_View_Entries(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_get_all_entries(self):
        """ a test for getting all entries """
        response = self.app.post("/api/v1/diaries",
                                content_type='application/json',
                                data=json.dumps(dict(id="1", title="Coding", content="The best way of life is code", today="17.07.2018"),)
                                )
                  
        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/diaries",
                                content_type='application/json', data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(reply2["message"],"All entries successfully viewed")


    def test_get_single_diary(self):
        '''Test to fetch single diary'''
        response = self.app.post("/api/v1/diaries",
                                content_type='application/json',
                                data=json.dumps(dict(id="1", title="Coding", content="The best way of life is code", today="17.07.2018"),)
                                )     
            
        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/diaries/1",
                                content_type='application/json', data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(reply2["message"],"Single entry successfully viewed")


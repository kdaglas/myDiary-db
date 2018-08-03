import unittest
from run import app
from flask import jsonify, json
from app.models import DiaryEntry
from app import views
from app.database.dbController import DatabaseConnection

my_connection = DatabaseConnection()


class Test_View_Entries(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config["TESTING"] = True
        # tear_down
        my_connection.delete_tables()
        my_connection.create_tables()

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
        self.assertEquals(reply2["message"], "All entries successfully viewed")

    def test_get_single_diary(self):
        '''Test to fetch single diary'''
        response = self.app.post("/api/v1/diaries",
                                content_type='application/json',
                                data=json.dumps(dict(id="1", title="Coding", content="The best way of life is code", today="17.07.2018"),)
                                )

        # was actually commented out
        # response = self.app.get("/api/v1/diaries",
        #                         content_type='application/json',
        #                         data=json.dumps(dict(id="2", title="Playing", content="The best way of life is playing", today="18.07.2018"),)
        #                         )

        reply = json.loads(response.data.decode())
        response2 = self.app.get("/api/v1/diaries/1",
        content_type='application/json',
            data=reply)
        reply2 = json.loads(response2.data.decode())
        self.assertEquals(reply2["message"], "Single entry successfully viewed")

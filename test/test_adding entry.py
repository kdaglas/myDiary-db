import unittest
from run import app
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
from flask import Flask
from flask_jwt_extended import JWTManager
import datetime


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'my-secret'
app.config['JWT_ACCESS_TOKEN EXPIRES'] = datetime.timedelta(days=2)
jwt = JWTManager(app)

from app import views

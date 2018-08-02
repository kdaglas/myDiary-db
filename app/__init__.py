from flask import Flask
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'my-secret'
jwt = JWTManager(app)

from app import views

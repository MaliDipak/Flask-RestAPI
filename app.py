from flask import Flask
from view.home import data
from flask_cors import CORS

app = Flask(__name__)

CORS(app)  # Enable CORS for all routes in the app

@app.route("/")
def index():
    return data

from controller import userController
from flask import Flask

app = Flask(__name__)

from app import routes # Calling this after the flask app instance is created because it is required in routes

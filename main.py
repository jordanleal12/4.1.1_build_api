"""Main module for running the flask application"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

ma = Marshmallow()  # Creates marshmallow object, allowing schema use

db = SQLAlchemy()


def create_app():
    """Creates flask app object"""
    app = Flask(__name__)

    app.config.from_object("config.app_config")  # Configures the app

    db.init_app(app)  # Initializes the database object with the flask app

    ma.init_app(app)  # Creating instance of Marshmallow, passing it our app

    return app

"""Main module for running the flask application"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    """Creates flask app object"""
    app = Flask(__name__)

    app.config.from_object("config.app.config")  # Configures the app

    db = SQLAlchemy(app)  # Creates database object

    return app

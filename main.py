"""Main module for running the flask application"""

from flask import Flask
from flask_marshmallow import Marshmallow
from cli import create_table, drop_table, seed_data
from extensions import db

ma = Marshmallow()  # Creates marshmallow object, allowing schema use


def create_app():
    """Creates flask app object"""
    app = Flask(__name__)

    app.config.from_object("config.app_config")  # Configures the app

    db.init_app(app)  # Initializes the database object with the flask app

    ma.init_app(app)  # Creating instance of Marshmallow, passing it our app

    app.cli.add_command(create_table)
    app.cli.add_command(drop_table)
    app.cli.add_command(seed_data)

    return app

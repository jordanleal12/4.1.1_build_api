"""Main module for running the flask application"""

from flask import Flask
from flask_marshmallow import Marshmallow
from extensions import db

ma = Marshmallow()  # Creates marshmallow object, allowing schema use


def create_app():
    """Creates flask app object"""
    app = Flask(__name__)
    app.json.sort_keys = False
    app.config.from_object("config.app_config")  # Configures the app

    db.init_app(app)  # Initializes the database object with the flask app

    ma.init_app(app)  # Creating instance of Marshmallow, passing it our app

    from cli_commands import registerable_cli_commands

    for command in registerable_cli_commands:
        app.cli.add_command(command)

    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)

    return app

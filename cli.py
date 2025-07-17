import click
from flask.cli import with_appcontext
from models import Card  # Competition, Participant
from extensions import db
from datetime import date


@click.command("create")
@with_appcontext
def create_table():
    db.create_all()
    click.echo("Tables created.")


@click.command("drop")
@with_appcontext
def drop_table():
    db.drop_all()
    click.echo("🗑️ Tables dropped.")


@click.command("seed")
@with_appcontext
def seed_data():
    card1 = Card(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        title="Start the project",
        description="Stage 1, creating the database",
        status="To Do",
        priority="High",
        date=date.today(),
    )
    card2 = Card(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        title="SQLAlchemy and Marshmallow",
        description="Stage 2, integrate both modules in the project",
        status="Ongoing",
        priority="High",
        date=date.today(),
    )
    db.session.add_all([card1, card2])
    db.session.commit()
    click.echo("🌱 Seed data inserted.")

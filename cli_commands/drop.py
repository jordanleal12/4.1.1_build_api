import click
from flask.cli import with_appcontext
from extensions import db


@click.command("drop")
@with_appcontext
def drop_table():
    db.drop_all()
    click.echo("🗑️ Tables dropped.")

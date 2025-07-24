import click
from flask.cli import with_appcontext
from models import Category, Competition, Participant, Participation
from extensions import db


@click.command("seed")
@with_appcontext
def seed_data():
    cat1 = Category(title="sports", description="physical/athletic sports")
    cat2 = Category(title="quiz", description="different types of quiz competitions")
    db.session.add_all([cat1, cat2])
    db.session.commit()

    comp1 = Competition(
        title="Fifa World Cup",
        description="The world cup of football",
        prize="20 million",
        year=2024,
        # Directly sets the foreign key, requires foreign key id to already be committed
        category_id=cat1.id,
    )
    comp2 = Competition(
        title="Australian Football League",
        description="The league for Australian Football",
        prize="20 Million",
        year=2020,
        # OOP, links comp2 object and cat1 object, sqlalchemy automatically assigns foreign key
        # regardless of commit status, automatically maintains relationship both ways
        category=cat1,
    )
    db.session.add_all([comp1, comp2])

    participant1 = Participant(
        name="Participant 1", address="One Street, Suburb1", phone="0412345678"
    )
    participant2 = Participant(
        name="Participant2", address="Two Street, Suburb2", phone="0487654321"
    )
    db.session.add_all([participant1, participant2])

    participation1 = Participation(rank=1, competition=comp1, participant=participant1)
    participation2 = Participation(rank=7, competition=comp1, participant=participant2)
    db.session.add_all([participation1, participation2])

    db.session.commit()
    click.echo("🌱 Seed data inserted.")

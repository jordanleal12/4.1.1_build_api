"""Model for creating participants table"""

from extensions import db


class Participant(db.Model):
    __tablename__ = "Participants"  # Creates table name

    id = db.Column(
        db.Integer, primary_key=True
    )  # Creates id column as integer + primary key
    name = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)

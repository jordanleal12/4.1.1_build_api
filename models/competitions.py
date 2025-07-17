"""Model for creating competition table"""

from extensions import db


class Competition(db.Model):
    """Model for creating table in sql"""

    __tablename__ = "competitions"  # Creates table name
    id = db.Column(
        db.Integer, primary_key=True
    )  # Creates id column as integer + primary key
    title = db.Column(db.String())
    description = db.Column(db.String())
    prize = db.Column(db.String())
    year = db.Column(db.Integer)

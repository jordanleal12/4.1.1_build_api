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
    # Foreign key for many (competition) to one (categories) relationship
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    # 'back_populates' requires db.relationship on both child and parent tables
    category = db.relationship("Category", back_populates="competitions")
    participations = db.relationship("Participation", back_populates="competition")

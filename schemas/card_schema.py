from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from extensions import db  # ma
from models.card import Card

# class CompetitionSchema(ma.Schema):
#     class Meta:
#         fields = ("id", "title", "description", "prize", "year")


class CardSchema(SQLAlchemyAutoSchema):
    """Schema for Card Model using SQLAlchemy Auto Schema"""

    class Meta:
        """Assigns Card model as model"""

        model = Card
        sqla_session = db.session
        load_instance = True


card_schema = CardSchema()

cards_schema = CardSchema(many=True)

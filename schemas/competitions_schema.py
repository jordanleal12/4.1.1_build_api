"""Creates Schema for Competition model using Auto Schema"""

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from extensions import db  # ma
from models.competitions import Competition

# class CompetitionSchema(ma.Schema):
#     class Meta:
#         fields = ("id", "title", "description", "prize", "year")


class CompetitionSchema(SQLAlchemyAutoSchema):
    """Schema for Competition Model using SQLAlchemy Auto Schema"""

    class Meta:
        """Assigns Competition model as model"""

        model = Competition
        sqla_session = db.session
        load_instance = True


competition_schema = CompetitionSchema()

competitions_schema = CompetitionSchema(many=True)

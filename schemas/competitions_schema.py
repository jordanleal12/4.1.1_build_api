"""Creates Schema for Competition model using Auto Schema"""

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from extensions import db
from models import Competition

# class CompetitionSchema(ma.Schema):
#     class Meta:
#         fields = ("id", "title", "description", "prize", "year")


class CompetitionSchema(SQLAlchemyAutoSchema):
    """Schema for Competition Model using SQLAlchemy Auto Schema"""

    category = fields.Nested("CategorySchema", only=("title",))
    participations = fields.List(
        fields.Nested("ParticipationSchema", exclude=("competition",))
    )

    class Meta:
        """Assigns Competition model as model"""

        model = Competition
        include_fk = True
        load_only = ("category_id",)
        fields = (
            "id",
            "title",
            "description",
            "prize",
            "year",
            "category",
            "participations",
        )
        sqla_session = db.session
        load_instance = True


competition_schema = CompetitionSchema()

competitions_schema = CompetitionSchema(many=True)

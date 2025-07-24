from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from models import Participation
from extensions import db


class ParticipationSchema(SQLAlchemyAutoSchema):
    competition = fields.Nested("CompetitionSchema", only=("title", "year"))

    participant = fields.Nested("ParticipantSchema", only=("name", "address"))

    class Meta:

        model = Participation
        include_fk = True
        include_relationships = True
        fields = ("id", "rank", "competition", "participant", "participant_id")
        load_only = ("participant_id",)
        sqla_session = db.session
        load_instance = True


participation_schema = ParticipationSchema()
participations_schema = ParticipationSchema(many=True)

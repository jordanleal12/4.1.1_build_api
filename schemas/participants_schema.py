"""Creates Schema for Participants model using Auto Schema"""

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from extensions import db  # ma
from models.participants import Participant

# class ParticipantSchema(ma.Schema):
#     class Meta:
#         fields = ("id", "name", "address", "phone")


class ParticipantSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Participant
        sqla_session = db.session
        load_instance = True


participant_schema = ParticipantSchema()

participants_schema = ParticipantSchema(many=True)

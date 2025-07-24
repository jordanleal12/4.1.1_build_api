from flask import Blueprint, jsonify, request, abort
from main import db
from models import Participant
from schemas import participant_schema, participants_schema

participants = Blueprint("participants", __name__, url_prefix="/participants")


@participants.route("/", methods=["GET"])
def get_participants():
    stmt = db.select(Participant)
    participants_list = db.session.scalars(stmt)
    result = participants_schema.dump(participants_list)
    return jsonify(result)


@participants.route("/", methods=["POST"])
def create_participant():
    participant_fields = participant_schema.load(request.json)
    new_participant = Participant(
        name=participant_fields.name,
        address=participant_fields.address,
        phone=participant_fields.phone,
    )
    db.session.add(new_participant)
    db.session.commit()
    return jsonify(participant_schema.dump(new_participant))


@participants.route("/<int:id>/", methods=["DELETE"])
def delete_participant(id):
    stmt = db.select(Participant).filter_by(id=id)
    participant = db.session.scalar(stmt)

    if not participant:
        return abort(400, description="Participant doesn't exist")
    db.session.delete(participant)
    db.session.commit()
    return jsonify(participant_schema.dump(participant))

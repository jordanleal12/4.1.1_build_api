from flask import Blueprint, jsonify, request, abort
from main import db
from models import Participation
from schemas import participation_schema, participations_schema

participations = Blueprint("participations", __name__, url_prefix="/participations")


@participations.route("/", methods=["GET"])
def get_participations():
    stmt = db.select(Participation)
    participations_list = db.session.scalars(stmt)
    result = participations_schema.dump(participations_list)
    return jsonify(result)


@participations.route("/<int:participation_id>", methods=["GET"])
def get_participation(participation_id):
    stmt = db.select(Participation).filter_by(id=participation_id)
    participation = db.session.scalar(stmt)

    if not participation:
        return abort(400, description="Participation does not exist")

    result = participation_schema.dump(participation)
    return jsonify(result)


@participations.route("/<int:id>/", methods=["DELETE"])
def delete_participation(id):
    stmt = db.select(Participation).filter_by(id=id)
    participation = db.session.scalar(stmt)

    if not participation:
        return abort(400, description="Participation doesn't exist")
    db.session.delete(participation)
    db.session.commit()
    return jsonify(participation_schema.dump(participation))

from flask import Blueprint, jsonify, request, abort
from main import db
from models import Competition, Participation, Participant
from schemas import competitions_schema, competition_schema, participation_schema

competitions = Blueprint("competitions", __name__, url_prefix="/competitions")


@competitions.route("/", methods=["GET"])
def get_competitions():
    stmt = db.select(Competition)
    competitions_list = db.session.scalars(stmt)
    result = competitions_schema.dump(competitions_list)
    return jsonify(result)


@competitions.route("/<int:comp_id>/", methods=["GET"])
def get_competition(comp_id):
    stmt = db.select(Competition).filter_by(id=comp_id)
    competition = db.session.scalar(stmt)

    if not competition:
        return abort(400, description="Competition does not exist")
    result = competition_schema.dump(competition)
    return jsonify(result)


@competitions.route("/", methods=["POST"])
def create_competitions():
    competition_fields = competition_schema.load(request.json)

    new_competition = Competition(
        title=competition_fields.title,
        description=competition_fields.description,
        prize=competition_fields.prize,
        year=competition_fields.year,
        category_id=competition_fields.category_id,
    )
    db.session.add(new_competition)
    db.session.commit()
    return jsonify(competition_schema.dump(new_competition))


@competitions.route("/<int:comp_id>/", methods=["DELETE"])
def delete_competition(comp_id):
    stmt = db.select(Competition).filter_by(id=comp_id)
    competition = db.session.scalar(stmt)
    if not competition:
        return abort(400, description="Competition doesn't exist")
    db.session.delete(competition)
    db.session.commit()
    return jsonify(competition_schema.dump(competition))


@competitions.route("/<int:comp_id>/", methods=["PUT"])
def update_competition(comp_id):
    competition_fields = request.get_json()

    stmt = db.select(Competition).filter_by(id=comp_id)
    competition = db.session.scalar(stmt)

    if not competition:
        return abort(400, description="Competition does not exist")
    competition.title = competition_fields["title"]
    competition.description = competition_fields["description"]
    competition.prize = competition_fields["prize"]
    competition.year = competition_fields["year"]
    db.session.commit()
    return jsonify(competition_schema.dump(competition))


@competitions.route("/search", methods=["GET"])
def search_competitions():
    competitions_list = []
    if request.args.get("year"):
        stmt = db.select(Competition).filter_by(year=request.args.get("year"))
        competitions_list = db.session.scalars(stmt)
    elif request.args.get("prize"):
        stmt = db.select(Competition).filter_by(prize=request.args.get("prize"))
        competitions_list = db.session.scalars(stmt)
    result = competitions_schema.dump(competitions_list)
    return jsonify(result)


@competitions.route("/<int:comp_id>/participations", methods=["POST"])
def create_participation(comp_id):
    # Get participation fields from request body
    participation_fields = participation_schema.load(request.json)
    # Get participant id from request body and load participant data
    participant_id = participation_fields.participant_id
    stmt = db.select(Participant).filter_by(id=participant_id)
    participant = db.session.scalar(stmt)
    # Check participant exists
    if not participant:
        return abort(400, description="Invalid participant")

    # Get competition from comp id in url
    stmt = db.select(Competition).filter_by(id=comp_id)
    competition = db.session.scalar(stmt)
    # Check competition exists
    if not competition:
        return abort(400, description="Competition does not exist")

    # Create new participation from competition and participant data
    new_participation = Participation(
        participant_id=participant.id, competition_id=competition.id
    )
    db.session.add(new_participation)
    db.session.commit()
    return jsonify(participation_schema.dump(new_participation))


@competitions.route(
    "/<int:comp_id>/participations/<int:participation_id>", methods=["PUT", "PATCH"]
)
def update_participation(comp_id, participation_id):
    updated_fields = participation_schema.load(request.json)

    # Check for valid participant
    participant_id = updated_fields.participant_id
    stmt = db.select(Participant).filter_by(id=participant_id)
    participant = db.session.scalar(stmt)
    if not participant:
        return abort(400, description="Invalid participant")

    # Check for valid competition
    stmt = db.select(Competition).filter_by(id=comp_id)
    competition = db.session.scalar(stmt)
    if not competition:
        return abort(400, description="Competition does not exist")

    # Check for valid participation
    stmt = db.select(Participation).filter_by(id=participation_id)
    participation = db.session.scalar(stmt)
    if not participation:
        return abort(400, description="Participation does not exist")

    # Assign updated fields
    participation.rank = updated_fields.rank or participation.rank
    participation.competition_id = competition.id or participation.competition_id
    participation.participant_id = participant.id or participation.participant_id
    db.session.add(participation)
    db.session.commit()
    return jsonify(participation_schema.dump(participation))

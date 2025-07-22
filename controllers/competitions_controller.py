from flask import Blueprint, jsonify, request, abort
from main import db
from models import Competition
from schemas import competitions_schema, competition_schema

competitions = Blueprint("competitions", __name__, url_prefix="/competitions")


@competitions.route("/", methods=["GET"])
def get_competitions():
    stmt = db.select(Competition)
    competitions_list = db.session.scalars(stmt)
    result = competitions_schema.dump(competitions_list)
    return jsonify(result)


@competitions.route("/<int:id>/", methods=["GET"])
def get_competition(id):
    stmt = db.select(Competition).filter_by(id=id)
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
    )
    db.session.add(new_competition)
    db.session.commit()
    return jsonify(competition_schema.dump(new_competition))


@competitions.route("/<int:id>/", methods=["DELETE"])
def delete_competition(id):
    stmt = db.select(Competition).filter_by(id=id)
    competition = db.session.scalar(stmt)
    if not competition:
        return abort(400, description="Competition doesn't exist")
    db.session.delete(competition)
    db.session.commit()
    return jsonify(competition_schema.dump(competition))


@competitions.route("/<int:id>/", methods=["PUT"])
def update_competition(id):
    competition_fields = request.get_json()

    stmt = db.select(Competition).filter_by(id=id)
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

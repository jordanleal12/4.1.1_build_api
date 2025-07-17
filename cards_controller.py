from datetime import date
from flask import Blueprint, jsonify, request, abort
from extensions import db
from models import Card
from schemas.card_schema import card_schema, cards_schema

cards = Blueprint("cards", __name__, url_prefix="/cards")


@cards.route("/", methods=["GET"])
def get_cards():
    stmt = db.select(Card)
    cards_list = db.session.scalars(stmt)
    result = cards_schema.dump(cards_list)
    return jsonify(result)


@cards.route("/", methods=["POST"])
def create_card():
    card_fields = card_schema.load(request.json)
    new_card = Card()
    new_card.title = card_fields["title"]
    new_card.description = card_fields["description"]
    new_card.status = card_fields["status"]
    new_card.priority = card_fields["priority"]
    new_card.date = date.today()

    db.session.add(new_card)
    db.session.commit()

    return jsonify(card_schema.dump(new_card))


@cards.route("/<int:card_id>/", methods=["DELETE"])
def delete_card(card_id):
    stmt = db.select(Card).filter_by(id=card_id)
    card = db.session.scalar(stmt)

    if not card:
        return abort(400, description="Card doesn't exist")
    db.session.delete(card)
    db.session.commit()

    return jsonify(card_schema.dump(card))

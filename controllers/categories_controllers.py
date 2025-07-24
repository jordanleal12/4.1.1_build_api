from flask import Blueprint, jsonify, request, abort
from models import Category
from extensions import db
from schemas import categories_schema, category_schema

categories = Blueprint("categories", __name__, url_prefix="/categories")


@categories.route("/", methods=["GET"])
def get_categories():
    stmt = db.select(Category)
    categories_list = db.session.scalars(stmt)

    if not categories_list:
        return abort(400, description="Category does not exist")

    data = categories_schema.dump(categories_list)
    return jsonify(data), 200


@categories.route("/<int:cat_id>/", methods=["GET"])
def get_category(cat_id):
    stmt = db.select(Category).filter_by(id=cat_id)
    category = db.session.scalar(stmt)

    if not category:
        return abort(400, description="Category does not exist")

    result = category_schema.dump(category)
    return jsonify(result), 200


@categories.route("/", methods=["POST"])
def create_categories():
    category_fields = category_schema.load(request.json)

    new_category = Category(
        title=category_fields.title, description=category_fields.description
    )
    db.session.add(new_category)
    db.session.commit()
    return jsonify(category_schema.dump(new_category)), 201


@categories.route("/<int:cat_id>/", methods=["DELETE"])
def delete_category(cat_id):
    stmt = db.select(Category).filter_by(id=cat_id)
    category = db.session.scalar(stmt)
    if not category:
        return abort(400, description="Category doesn't exist")
    db.session.delete(category)
    db.session.commit()
    return jsonify(category_schema.dump(category)), 200


@categories.route("/<int:cat_id>/", methods=["PUT"])
def update_category(cat_id):
    category_fields = request.get_json()

    stmt = db.select(Category).filter_by(id=cat_id)
    category = db.session.scalar(stmt)

    if not category:
        return abort(400, description="Category does not exist")
    category.title = category_fields["title"]
    category.description = category_fields["description"]
    category.prize = category_fields["prize"]
    category.year = category_fields["year"]
    db.session.commit()
    return jsonify(category_schema.dump(category)), 200

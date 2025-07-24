"""Creates Schema for Category model using Auto Schema"""

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from extensions import db
from models import Category


class CategorySchema(SQLAlchemyAutoSchema):
    """Schema for Category Model using SQLAlchemy Auto Schema"""

    # Many=True required nesting with 1 to many relationships
    competitions = fields.Nested("CompetitionSchema", many=True, only=("title", "year"))

    class Meta:
        """Assigns object relationships and database connections"""

        model = Category
        ordered = True
        fields = ("id", "title", "description", "competitions")
        include_relationships = True
        sqla_session = db.session
        load_instance = True


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

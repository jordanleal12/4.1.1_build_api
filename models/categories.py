from extensions import db


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    description = db.Column(db.String())
    # 'back_populates' requires db.relationship on both child and parent tables
    # Cascade declared on the parent table only
    competitions = db.relationship(
        "Competition", back_populates="category", cascade="all, delete"
    )

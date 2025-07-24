from extensions import db


class Participation(db.Model):
    __tablename__ = "participations"
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer)
    competition_id = db.Column(
        db.Integer, db.ForeignKey("competitions.id"), nullable=False
    )
    participant_id = db.Column(
        db.Integer, db.ForeignKey("participants.id"), nullable=False
    )
    competition = db.relationship("Competition", back_populates="participations")
    participant = db.relationship("Participant", back_populates="participations")

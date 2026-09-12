from datetime import datetime

from app import db


class Reservation(db.Model):
    __tablename__ = "reservations"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    guest_id = db.Column(
        db.Integer,
        db.ForeignKey("guests.id"),
        nullable=False
    )

    gift_id = db.Column(
        db.Integer,
        db.ForeignKey("gifts.id"),
        nullable=False,
        unique=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    guest = db.relationship(
        "Guest",
        back_populates="reservations"
    )

    gift = db.relationship(
        "Gift",
        back_populates="reservation"
    )
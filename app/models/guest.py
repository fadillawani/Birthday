from datetime import datetime

from app import db


class Guest(db.Model):
    __tablename__ = "guests"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(150),
        nullable=False
    )

    email = db.Column(
        db.String(255),
        nullable=False,
        unique=True
    )

    rsvp_status = db.Column(
        db.String(20),
        nullable=True
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    reservations = db.relationship(
        "Reservation",
        back_populates="guest",
        cascade="all, delete-orphan"
    )
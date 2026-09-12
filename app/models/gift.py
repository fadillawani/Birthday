from datetime import datetime

from app import db


class Gift(db.Model):
    __tablename__ = "gifts"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(255),
        nullable=False
    )

    description = db.Column(
        db.Text
    )

    category = db.Column(
        db.String(100)
    )

    image = db.Column(
        db.String(255)
    )

    product_url = db.Column(
        db.Text
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    reservation = db.relationship(
        "Reservation",
        back_populates="gift",
        uselist=False,
        cascade="all, delete-orphan"
    )
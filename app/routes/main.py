from flask import Blueprint, render_template

from app.models.gift import Gift
from app.models.reservation import Reservation


main_bp = Blueprint("main", __name__)


@main_bp.route("/")
def home():
    return render_template("index.html")


@main_bp.route("/wishlist")
def wishlist():

    gifts = Gift.query.order_by(Gift.id.asc()).all()

    reservations = Reservation.query.all()

    reserved_gifts = {
        reservation.gift_id
        for reservation in reservations
    }

    return render_template(
        "wishlist.html",
        gifts=gifts,
        reserved_gifts=reserved_gifts
    )
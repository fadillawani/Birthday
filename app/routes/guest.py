from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session
)

from sqlalchemy.exc import IntegrityError

from app import db
from app.models.guest import Guest
from app.models.reservation import Reservation
from app.models.gift import Gift


guest_bp = Blueprint("guest", __name__)


@guest_bp.route("/guest", methods=["GET"])
def guest():
    return render_template("guest.html")


@guest_bp.route("/invitation", methods=["POST"])
def create_invitation():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()

    if not name or not email:
        return redirect(url_for("guest.guest"))

    # Vérifier si l'invité existe déjà
    guest = Guest.query.filter_by(email=email).first()

    if guest is None:

        guest = Guest(
            name=name,
            email=email
        )

        db.session.add(guest)
        db.session.commit()

    else:

        # Mettre à jour le nom si nécessaire
        guest.name = name

        db.session.commit()

    # On garde uniquement l'ID en session
    session["guest_id"] = guest.id

    return redirect(url_for("guest.invitation"))


@guest_bp.route("/invitation", methods=["GET"])
def invitation():

    guest_id = session.get("guest_id")

    if not guest_id:
        return redirect(url_for("guest.guest"))

    guest = db.session.get(Guest, guest_id)

    if guest is None:
        session.pop("guest_id", None)
        return redirect(url_for("guest.guest"))

    return render_template(
        "invitation.html",
        guest=guest
    )


@guest_bp.route("/rsvp", methods=["POST"])
def rsvp():

    guest_id = session.get("guest_id")

    if not guest_id:
        return redirect(url_for("guest.guest"))

    response = request.form.get("response")

    if response not in ["yes", "maybe", "no"]:
        return redirect(url_for("guest.invitation"))

    guest = db.session.get(Guest, guest_id)

    if guest is None:
        session.pop("guest_id", None)
        return redirect(url_for("guest.guest"))

    guest.rsvp_status = response

    db.session.commit()

    return redirect(url_for("main.wishlist"))


@guest_bp.route("/reserve/<int:gift_id>", methods=["POST"])
def reserve_gift(gift_id):

    guest_id = session.get("guest_id")

    if not guest_id:
        return redirect(url_for("guest.guest"))

    guest = db.session.get(Guest, guest_id)

    if guest is None:
        session.pop("guest_id", None)
        return redirect(url_for("guest.guest"))

    gift = db.session.get(Gift, gift_id)

    if gift is None:
        return redirect(url_for("main.wishlist"))

    # Vérifier si le cadeau est déjà réservé
    existing_reservation = Reservation.query.filter_by(
        gift_id=gift_id
    ).first()

    if existing_reservation:
        return redirect(url_for("main.wishlist"))

    reservation = Reservation(
        guest_id=guest_id,
        gift_id=gift_id
    )

    try:

        db.session.add(reservation)
        db.session.commit()

    except IntegrityError:

        db.session.rollback()

    return redirect(url_for("main.wishlist"))
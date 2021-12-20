from flask import Blueprint

bp = Blueprint("home", __name__)


@bp.route("/", methods=["GET"])
def home():
    return {"message": "This is our affiliate dashboard API"}

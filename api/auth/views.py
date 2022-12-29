from flask import Blueprint, request

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login/", methods=["POST"])
def login():
    pass


@bp.route("/signup/", methods=["POST"])
def signup():
    pass

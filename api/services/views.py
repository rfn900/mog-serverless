from flask import Blueprint

bp = Blueprint("services", __name__, url_prefix="/services")


@bp.route("/", methods=["GET"])
def service():
    return {"message": "Services endpoint"}

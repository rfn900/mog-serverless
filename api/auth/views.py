from flask import Blueprint, request
from marshmallow import ValidationError
from werkzeug.security import generate_password_hash
from api.auth.controllers.login_user import (
    check_password_and_get_token,
    validates_data,
    retrieve_user_by_email,
)
from api.auth.controllers.signup_user import (
    check_if_user_exists,
    register_user,
    retrieve_formatted_data,
    validate_and_return_data,
)
from utils.logger import logger


bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login/", methods=["POST"])
def login():
    payload = validates_data(request.json)
    if not payload:
        # returns 401 if any email or / and password is missing
        return {"success": False, "message": "Email and Password can't be empty"}, 401

    user = retrieve_user_by_email(email=payload["email"])

    if not user:
        # returns 401 if user does not exist
        return {"success": False, "message": "user not found"}, 401

    token = check_password_and_get_token(
        user["password"], payload["email"], payload["password"]
    )

    if token:
        return {"success": True, "data": {"token": token.decode("UTF-8")}}

    # returns 403 if password is wrong
    return {"success": False, "message": "Wrong password or email"}, 403


@bp.route("/signup/", methods=["POST"])
def signup():
    # creates a dictionary of the form data
    try:
        data = validate_and_return_data(request.json)
        formatted_data = retrieve_formatted_data(data)
        email = formatted_data["email"]
        logger.debug(
            formatted_data["password"],
            generate_password_hash(formatted_data["password"]),
        )
        user_exists = check_if_user_exists(email)
        if not user_exists:
            return register_user(formatted_data)
        return {"success": False, "message": "User already exists"}, 202
    except ValidationError as e:
        return {"success": False, "message": e.messages}, 400

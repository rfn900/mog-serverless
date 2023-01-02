from flask import Blueprint, request
import jwt
from marshmallow import ValidationError
from werkzeug.exceptions import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import os
from api.auth.model import User
from api.auth.schemas import UserSchema
from datetime import datetime, timedelta

from utils.logger import logger

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login/", methods=["POST"])
def login():
    # creates dictionary of form data
    auth = request.json
    password, email = auth.get("password"), auth.get("email")

    if not auth or not email or not password:
        # returns 401 if any email or / and password is missing
        return {"success": False, "message": "Email and Password can't be empty"}, 401

    user = User()
    existing_user = user.retrieve_user_by_email(email=email)

    if not existing_user:
        # returns 401 if user does not exist
        return {"success": False, "message": "user not found"}, 401
    logger.debug(existing_user)
    if check_password_hash(existing_user.get("password"), password):
        # generates the JWT Token
        token = jwt.encode(
            {
                "email": existing_user.get("email"),
                "exp": datetime.utcnow() + timedelta(days=7),
            },
            os.environ.get("SECRET_KEY") or "",
        )

        return {"success": True, "data": {"token": token.decode("UTF-8")}}, 403
    # returns 403 if password is wrong
    return {"success": False, "message": "Wrong password or email"}, 403


@bp.route("/signup/", methods=["POST"])
def signup():
    # creates a dictionary of the form data
    data = {}
    try:
        data = UserSchema().load(request.json)
    except ValidationError as e:
        return {"success": False, "message": e.messages}, 400

    name, email = data.get("name"), data.get("email")
    username, password = data.get("username"), data.get("password")

    # checking for existing user
    user = User()
    existing_user = user.retrieve_user_by_email(email=email)
    if not existing_user:
        user.set_new_user(
            name=name,
            email=email,
            username=username,
            password=generate_password_hash(password),
        )
        try:
            user.save_user()
            return {"success": True, "message": "Successfully added user"}, 201
        except:
            return {"success": False, "message": "Error saving user"}, 500

    return {"success": False, "message": "User already exists"}, 202

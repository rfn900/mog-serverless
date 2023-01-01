from flask import Blueprint, make_response, request
from marshmallow import ValidationError
from werkzeug.security import generate_password_hash
from api.auth.model import User
from api.auth.schemas import UserSchema

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login/", methods=["POST"])
def login():
    pass


@bp.route("/signup/", methods=["POST"])
def signup():
    # creates a dictionary of the form data
    data = {}
    try:
        data = UserSchema().load(request.json)
    except ValidationError as e:
        return make_response(e.messages, 403)

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

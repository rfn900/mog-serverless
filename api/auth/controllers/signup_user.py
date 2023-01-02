from werkzeug.security import generate_password_hash
from api.auth.model import User
from api.auth.schemas import UserSchema


def validate_and_return_data(_data):
    return UserSchema().load(_data)


def retrieve_formatted_data(_data):
    return {
        "name": _data["name"],
        "email": _data["email"],
        "username": _data["username"],
        "password": _data["password"],
    }


def check_if_user_exists(email):
    user = User()
    existing_user = user.retrieve_user_by_email(email=email)
    if existing_user:
        return True
    return False


def register_user(user_data):
    user = User()
    user.set_new_user(
        name=user_data["name"],
        email=user_data["email"],
        username=user_data["username"],
        password=generate_password_hash(user_data["password"]),
    )
    try:
        user.save_user()
        return {"success": True, "message": "Successfully added user"}, 201
    except:
        return {"success": False, "message": "Error saving user"}, 500

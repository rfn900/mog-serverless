from datetime import timedelta
import jwt
from werkzeug.exceptions import datetime
from werkzeug.security import check_password_hash, generate_password_hash, os
from api.auth.model import User


def validates_data(data):
    password, email = data.get("password"), data.get("email")

    if not data or not password or not email:
        return False

    return {"email": data.get("email"), "password": data.get("password")}


def retrieve_user_by_email(email: str):
    user = User()
    current_user = user.retrieve_user_by_email(email=email)

    if current_user:
        return current_user

    return False


def check_password_and_get_token(password_hash, email, password):
    if check_password_hash(password_hash, password):
        # generates the JWT Token
        token = jwt.encode(
            {
                "email": email,
                "exp": datetime.utcnow() + timedelta(days=7),
            },
            os.environ.get("SECRET_KEY") or "",
        )
        return token
    return False

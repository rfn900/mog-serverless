from flask import request
import os

# imports for PyJWT authentication
import jwt
from functools import wraps

from api.auth.model import User


def extract_header(headers):
    token: str = headers["Authorization"].split(" ")[1]
    bearer_str: str = headers["Authorization"].split(" ")[0]
    return token, bearer_str


secret_key = os.environ.get("SECRET_KEY") or ""
# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        bearer_str = ""
        # jwt is passed in the request header
        if "Authorization" in request.headers:
            token, bearer_str = extract_header(request.headers)
        # return 401 if token is not passed
        if not token:
            return {"success": False, "message": "Token missing"}, 401
        if bearer_str != "Bearer":
            return {"success": False, "message": "Wrong header format"}, 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, secret_key)
            user = User()
            current_user = user.retrieve_user_by_email(email=data["email"])
        except jwt.ExpiredSignatureError:
            return {"success": False, "message": "Token has expired"}, 401
        except:
            return {"success": False, "message": "Something went wrong"}, 401
        # returns the current logged in users contex to the routes
        return f(current_user, *args, **kwargs)

    return decorated

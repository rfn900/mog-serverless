from flask import request, jsonify
import os

# imports for PyJWT authentication
import jwt
from functools import wraps

from api.auth.model import User

secret_key = os.environ.get("SECRET_KEY") or ""
# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if "x-access-token" in request.headers:
            token = request.headers["x-access-token"]
        # return 401 if token is not passed
        if not token:
            return jsonify({"message": "Token is missing !!"}), 401

        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, secret_key)
            user = User()
            current_user = user.retrieve_user_by_email(email=data["email"])
        except:
            return jsonify({"message": "Token is invalid !!"}), 401
        # returns the current logged in users contex to the routes
        return f(current_user, *args, **kwargs)

    return decorated

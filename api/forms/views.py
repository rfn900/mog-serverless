import json
from flask import Blueprint, Response, request
from marshmallow import ValidationError
from api.auth.controllers.decorators.token_required import token_required
from api.forms.controllers.post_contact import post_contact, validate_and_return_data
from api.forms.controllers.retrieve_contacts import retrieve_contacts
from bson import json_util


bp = Blueprint("forms", __name__, url_prefix="/forms")


@bp.route("/contact/", methods=["POST"])
@token_required
def contact(current_user):
    try:
        data = validate_and_return_data(request.json)
        contact_sent = post_contact(data)
        if contact_sent:
            return json.loads(json_util.dumps(data))
        else:
            return {"error": "Message not sent"}, 500
    except ValidationError as err:
        return err.messages, 400


@bp.route("/contacts/", methods=["GET"])
@token_required
def contacts(current_user):
    formatted_data = retrieve_contacts()
    return Response(json_util.dumps(formatted_data), mimetype="application/json")

from datetime import datetime
import json
from flask import Blueprint, Response, request
from marshmallow import ValidationError
from api.forms.controllers.send_email import send_email
from api.forms.model import Forms
from api.forms.schemas import ContactFormSchema
from bson import json_util
import uuid

from utils.logger import logger

bp = Blueprint("forms", __name__, url_prefix="/forms")


@bp.route("/contact/", methods=["POST"])
def contact():
    try:
        data = ContactFormSchema().load(request.json)
        data["dateSent"] = datetime.now().isoformat()
        data["id"] = str(uuid.uuid4())
        form = Forms()
        form.register_payload(data)
        form.save()
        send_email(data)
        data.pop("_id")
        return json.loads(json_util.dumps(data))  # All this to convert _id from mongo
    except ValidationError as err:
        return err.messages, 400


@bp.route("/contacts/", methods=["GET"])
def contacts():
    form = Forms()
    data = form.retrieve_saved_contacts()
    formatted_data = []
    for doc in data:
        doc.pop("_id")
        formatted_data.append(doc)
    return Response(json_util.dumps(formatted_data), mimetype="application/json")

import json
from flask import Blueprint, request
from marshmallow import ValidationError
from api.forms.model import Forms
from api.forms.schemas import ContactFormSchema
from utils.logger import logger
import bson.json_util as json_util

bp = Blueprint("forms", __name__, url_prefix="/forms")


@bp.route("/contact/", methods=["POST"])
def contact():
    try:
        data = ContactFormSchema().load(request.json)
        form = Forms(data)
        form.save()
        return json.loads(json_util.dumps(data))  # All this to convert _id from mongo
    except ValidationError as err:
        return err.messages, 400

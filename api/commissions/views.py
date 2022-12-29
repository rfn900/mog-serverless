from flask import Blueprint, request
from datetime import date
from .controllers.adtraction import pull_adtraction_data
from .controllers.adrecord import pull_adrecord_data
from .controllers.awin import pull_awin_data
from .controllers.tradedoubler import pull_tradedoubler_data

bp = Blueprint("commissions", __name__, url_prefix="/commissions")


def calculate_date_interval(d1string, d2string):
    from_date_arr = d1string.split("-")
    to_date_arr = d2string.split("-")
    from_date_obj = date(
        int(from_date_arr[0]), int(from_date_arr[1]), int(from_date_arr[2])
    )
    to_date_obj = date(int(to_date_arr[0]), int(to_date_arr[1]), int(to_date_arr[2]))
    delta = to_date_obj - from_date_obj
    return delta.days + 1


def extract_date(args):
    date_list = []
    today = date.today()
    if args:
        from_date = args["from"]
        to_date = args["to"]
    else:
        from_date = today
        to_date = today
    date_list.append(from_date)
    date_list.append(to_date)
    return date_list


@bp.route("/", methods=["GET"])
def home():
    return {"hello": "world"}


@bp.route("/adrecord/", methods=["GET"])
def adrecord():
    from_date, to_date = extract_date(request.args)
    data = pull_adrecord_data(from_date, to_date)
    return data


@bp.route("/adtraction/", methods=["GET"])
def adtraction():
    from_date, to_date = extract_date(request.args)
    data = pull_adtraction_data(from_date, to_date)
    return data


@bp.route("/awin/", methods=["GET"])
def awin():
    from_date, to_date = extract_date(request.args)
    data = pull_awin_data(from_date, to_date)
    return data


@bp.route("/tradedoubler/", methods=["GET"])
def tradedoubler():
    from_date, to_date = extract_date(request.args)
    date_interval = calculate_date_interval(str(from_date), str(to_date))
    if date_interval >= 20:
        interval_type = "month"
    else:
        interval_type = "day"

    data = pull_tradedoubler_data(str(from_date), str(to_date), interval_type)
    return data


@bp.route("/total/", methods=["GET"])
def get_total_commissions():
    from_date, to_date = extract_date(request.args)

    awin_data = pull_awin_data(from_date, to_date)
    adrecord_data = pull_adrecord_data(from_date, to_date)
    adtraction_data = pull_adtraction_data(from_date, to_date)
    date_interval = calculate_date_interval(str(from_date), str(to_date))
    # Tradedoubler only lists up to 20 results per request
    if date_interval >= 20:
        interval_type = "month"
    else:
        interval_type = "day"
    tradedoubler_data = pull_tradedoubler_data(
        str(from_date), str(to_date), interval_type
    )

    sum = (
        float(awin_data["commission"])
        + float(adrecord_data["commission"])
        + float(adtraction_data["commission"])
        + float(tradedoubler_data["commission"])
    )

    return {"program": "total", "commission": sum}

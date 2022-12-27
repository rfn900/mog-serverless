from datetime import date, timedelta
from api.models import Database
from api.commissions.controllers.adrecord import pull_adrecord_data
from api.commissions.controllers.adtraction import pull_adtraction_data
from api.commissions.controllers.awin import pull_awin_data
from api.commissions.controllers.tradedoubler import pull_tradedoubler_data


db = Database()
db.initialize()


def handler():
    # This works specifically for function scheduling for the 1st of every month
    last_of_the_month = date.today() - timedelta(days=1)
    dt = last_of_the_month
    first_of_the_month = date(dt.year, dt.month, 1)

    adrecord = pull_adrecord_data(str(first_of_the_month), str(last_of_the_month))

    adtraction = pull_adtraction_data(str(first_of_the_month), str(last_of_the_month))

    awin = pull_awin_data(str(first_of_the_month), str(last_of_the_month))

    tradedoubler = pull_tradedoubler_data(
        str(first_of_the_month), str(last_of_the_month), "month"
    )

    commissions = [
        {"program": "adtraction", "value": adtraction["commission"]},
        {"program": "tradedoubler", "value": tradedoubler["commission"]},
        {"program": "awin", "value": awin["commission"]},
        {"program": "adrecord", "value": adrecord["commission"]},
        {"program": "misc", "value": 0},  # For now...
    ]

    data = {"results": commissions, "date": str(last_of_the_month)}

    _ = db.save_commissions_to_db(data)

    return 1

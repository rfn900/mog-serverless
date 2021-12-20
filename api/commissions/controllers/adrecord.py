from api.models import Database
import requests
import os


def pull_adrecord_data(from_date, to_date):
    tkn = os.environ.get("ADRECORD_TOKEN")
    dateRange = (
        f"from={from_date}T00%3A00%3A00%2B01%3A00&to={to_date}T23%3A59%3A59%2B0%3A00"
    )
    limit = "limit=500"
    group = "group=day"
    url = f"https://api.v2.adrecord.com/statistics?{dateRange}&{limit}&apikey={tkn}&{group}"

    response = requests.get(url)

    res = response.json()
    sum = 0
    for item in res:
        if item["epc"] != 0:
            sum += item["transactions"]["commission"]

    return {"ad_program": "adrecord", "commission": sum}

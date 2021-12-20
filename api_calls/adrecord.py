import requests
import os


def pull_adrecord_data(from_date, to_date):
    tkn = os.environ.get('ADRECORD_TOKEN')
    dateRange = f"from={from_date}T00%3A00%3A00%2B01%3A00&to={to_date}T23%3A59%3A59%2B0%3A00"
    limit = "limit=500"
    group = "group=month"
    url = f"https://api.v2.adrecord.com/statistics?{dateRange}&{limit}&apikey={tkn}&{group}"

    response = requests.get(url)
    return response.json()

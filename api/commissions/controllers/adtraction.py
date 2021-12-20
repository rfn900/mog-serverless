import requests
import os


def pull_adtraction_data(from_date, to_date):

    values2 = (
        f"{{ \n"
        f' "fromDate": "{from_date}", \n'
        f' "toDate": "{to_date}", \n'
        f' "currency": "SEK", \n'
        f' "market": "SE", \n'
        f' "transactionStatus": 3 \n'
        f"}}"
    )

    tkn = os.environ.get("ADTRACTION_TOKEN")
    url = f"https://api.adtraction.com/v2/affiliate/statistics/?token={tkn}"
    headers = {"Content-Type": "application/json;charset=UTF-8"}

    response = requests.post(url, data=values2, headers=headers)

    data = response.json()

    return {"ad_program": "adtraction", "commission": data["commission"]}

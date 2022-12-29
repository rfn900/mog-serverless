import requests
import os


def pull_awin_data(from_date: str, to_date: str):
    dateRange = f"startDate={from_date}&endDate={to_date}"
    pub_id = os.environ.get("AWIN_USER_ID")
    geo = "region=SE"
    tzone = "Europe/Berlin"
    tkn = os.environ.get("AWIN_TOKEN")

    url = f"https://api.awin.com/publishers/{pub_id}/reports/advertiser?{dateRange}&{geo}&{tzone}"
    headers = {"Authorization": f"Bearer {tkn}"}
    response = requests.get(url, headers=headers)

    res = response.json()
    sum: int = 0
    for item in res:
        sum += item["totalComm"]

    return {"ad_program": "awin", "commission": str(sum)}

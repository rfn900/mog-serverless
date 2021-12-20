import requests
import base64
import os


def encodeStr(str):
    str_bytes = str.encode("ascii")

    base64_bytes = base64.b64encode(str_bytes)
    base64_string = base64_bytes.decode("ascii")

    return base64_string


def get_bearer_token():

    username = os.environ.get("TRADEDOUBLER_USERNAME")
    password = os.environ.get("TRADEDOUBLER_PASSWORD")
    client_id = os.environ.get("TRADEDOUBLER_CLIENT_ID")
    client_secret = os.environ.get("TRADEDOUBLER_CLIENT_SECRET")
    cl_credentials_enconded = encodeStr(f"{client_id}:{client_secret}")
    preurl = "https://connect.tradedoubler.com/uaa/oauth/token"
    url = f"{preurl}?grant_type=password&username={username}&password={password}"
    pre_aut_headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {cl_credentials_enconded}",
    }

    pre_auth_response = requests.post(url, headers=pre_aut_headers)

    return pre_auth_response.json()["access_token"]


def pull_tradedoubler_data(fromDate, toDate, interval_type):
    b_token = get_bearer_token()

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {b_token}"}

    from_date_tupple = fromDate.split("-")
    from_date = "".join(from_date_tupple)

    to_date_tupple = toDate.split("-")
    to_date = "".join(to_date_tupple)
    url = f"https://connect.tradedoubler.com/publisher/report/statistics?intervalType={interval_type}&reportType=date&fromDate={from_date}&toDate={to_date}"
    response = requests.get(url, headers=headers)
    data = response.json()

    sum = 0
    for item in data["items"]:
        sum += item["salesCommission"]

    return {"ad_program": "tradedoubler", "commission": sum}

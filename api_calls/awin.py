import requests
import os


def pull_awin_data(from_date, to_date):
    dateRange = f"startDate={from_date}&endDate={to_date}"
    pub_id = os.environ.get('AWIN_USER_ID')
    geo = "region=SE"
    tzone = "Europe/Berlin"
    tkn = os.environ.get('AWIN_TOKEN')

    url = f'https://api.awin.com/publishers/{pub_id}/reports/advertiser?{dateRange}&{geo}&{tzone}'
    headers = {
        "Authorization": f"Bearer {tkn}"
    }
    response = requests.get(url, headers=headers)
    print(response.status_code)

    return response.json()

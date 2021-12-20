from flask import Flask, jsonify
import datetime
from api_calls.adtraction import pull_adtraction_data
from api_calls.tradedoubler import pull_tradedoubler_data
from api_calls.awin import pull_awin_data
from api_calls.adrecord import pull_adrecord_data

app = Flask(__name__)

today = datetime.datetime.now()
# to_date = today.strftime("%Y-%m-%d")
to_date = "2021-06-30"
from_date = "2021-06-01"
# from_date = one_month_ago_date(today)


@app.route("/commissions/adrecord/")
def adrecord():
    res = pull_adrecord_data(from_date, to_date)
    data = []

    for item in res:
        if item['transactions']['commission'] != 0:
            data.append({
                'month': item['month'],
                'commission': item['transactions']['commission']
            })

    return jsonify(data)


@app.route("/commissions/awin/")
def awin():
    res = pull_awin_data(from_date, to_date)

    return jsonify(res)


@app.route("/commissions/adtraction/")
def adtraction():
    res = pull_adtraction_data(from_date, to_date)

    return res


@app.route("/commissions/tradedoubler/")
def tradedoubler():
    res = pull_tradedoubler_data(from_date, to_date)

    return res


@app.route("/")
def home():
    return ({"hello": "world"})


if __name__ == "__main__":
    app.run(debug=True)

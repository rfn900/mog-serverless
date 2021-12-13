import time
from db.models import Commission
from db.database import Database
from api_calls.adrecord import pull_adrecord_data
from api_calls.adtraction import pull_adtraction_data
from api_calls.awin import pull_awin_data

adt = pull_adtraction_data()
adr = pull_adrecord_data()
awin = pull_awin_data()


def save_commissions_to_db():
    while True:
        time.sleep(300)
        commission = Commission().set_commission(adr, adt, awin)
        Database.save_commissions_to_db(commission)

# def scrape_to_db_thread():
    # sleep_thread = threading.Thread(target=save_commissions_to_db)
    # sleep_thread.start()

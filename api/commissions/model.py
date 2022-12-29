from datetime import date
from api.models import Model

from utils.logger import logger

class Commissions(Model):
    def save_commissions_to_db(self, data):
        try:
            self.database.monthly_results.insert_one(data)
            return 1
        except:
            logger.error("Failed to add commissions to DB")
            return 2

    def load_monthly_results(self):
        return self.database.monthly_results.find()

    def save_mediavine_revenue(self, data):
        try:
            self.database.mediavine_revenue.insert_one(data)
        except:
            print(f"Failed to add mediavine revenue to DB on: {date.today()}")

from datetime import date

from marshmallow import ValidationError
from api.commissions.schema import CommissionPayloadSchema
from api.db import Database
from utils.logger import logger


class Commissions(Database):
    def __init__(self, data) -> None:
        super().initialize()
        super().connect_to_affiliate_db()
        try:
            self.data = CommissionPayloadSchema().load(data)
        except ValidationError as err:
            self.errorMessage = err.messages

    def save_commissions_to_db(self):
        try:
            if self.data:
                self.database.monthly_results.insert_one(self.data)
                logger.info("Add commissions to DB")
                return 0
            if self.errorMessage:
                logger.error(self.errorMessage)
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
            logger.error("Failed to add mediavine revenue to DB")

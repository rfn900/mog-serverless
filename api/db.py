from pymongo import MongoClient
import os
import logging

logger = logging.getLogger(__name__)


class Database:
    def initialize(self):
        self.uri = os.environ.get("MONGO_URI")
        try:
            self.client = MongoClient(self.uri)
            logger.info("Connected to DB")
        except:
            logger.error("Failed to connect to DB")

    def connect_to_affiliate_db(self):
        self.database = self.client.affiliate_report

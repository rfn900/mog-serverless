from pymongo import MongoClient
from datetime import date
import os


class Database:
    def initialize(self):
        self.uri = os.environ.get("MONGO_URI")
        try:
            client = MongoClient(self.uri)
            self.database = client.affiliate_report
            print("Connected to DB")
        except:
            print("Failed to connect to DB")

    def save_commissions_to_db(self, data):
        try:
            self.database.monthly_results.insert_one(data)
            print(f"Add commissions to DB on: {date.today()}")
            return 1
        except:
            print(f"Failed to add commissions to DB on: {date.today()}")

    def load_monthly_results(self):
        return self.database.monthly_results.find()

    def save_mediavine_revenue(self, data):
        try:
            self.database.mediavine_revenue.insert_one(data)
        except:
            print(f"Failed to add mediavine revenue to DB on: {date.today()}")

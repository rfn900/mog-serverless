from pymongo import MongoClient
from datetime import date
import os


class Database:
    def initialize(self):
        self.uri = os.environ.get("MONGO_URI")
        try:
            client = MongoClient(self.uri)
            self.database = client.affiliate_report
            print("Connected to db")
        except:
            print("Deu merda na DB")

    def save_commissions_to_db(self, data):
        try:
            self.database.monthly_results.insert_one(data)
            print(f"Add commissions to DB on: {date.today()}")
            return 1
        except:
            print("Deu merda na hora de inserir na DB")

    def load_monthly_results(self):
        print("Tentando listar tudo")
        return self.database.monthly_results.find()

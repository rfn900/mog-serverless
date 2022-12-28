from pymongo import MongoClient
import os


class Model:
    def initialize(self):
        self.uri = os.environ.get("MONGO_URI")
        try:
            client = MongoClient(self.uri)
            self.database = client.affiliate_report
            print("Connected to DB")
        except:
            print("Failed to connect to DB")

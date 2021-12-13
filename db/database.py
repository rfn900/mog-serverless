import pymongo
import os


class Database:
    @classmethod
    def initialize(cls):
        client = pymongo.MongoClient(
            f"{os.environ.get('MONGO_HOST')}:{os.environ.get('MONGO_PORT')}\
            /affiliate_report")
        cls.database = client.get_default_database()

    @ classmethod
    def save_commissions_to_db(cls, data):
        cls.database.commissions.insert_one(data)

    @ classmethod
    def load_from_db(cls):
        return cls.database.monthly_results.find()

from api import create_app
from pymongo import MongoClient
from utils.logger import logger
import os

app = create_app()

# Connect to DB
uri = os.environ.get("MONGO_URI")
try:
    db = MongoClient(uri)
    logger.info("Connected to DB")
except:
    logger.error("Failed to connect to DB")


if __name__ == "__main__":
    app.run(debug=True)

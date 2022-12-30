from api import create_app
from pymongo import MongoClient
from utils.logger import logger
from flask_mail import Mail
import os

app = create_app()
app.config["MAIL_SERVER"] = os.environ.get("EMAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("EMAIL_PORT")
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.environ.get("EMAIL_USER")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("EMAIL_USER")
app.config["MAIL_PASSWORD"] = os.environ.get("EMAIL_PASSWORD")


mail = Mail(app)

# Connect to DB
uri = os.environ.get("MONGO_URI")
try:
    db = MongoClient(uri)
    logger.info("Connected to DB")
except:
    logger.error("Failed to connect to DB")


if __name__ == "__main__":
    app.run(debug=True)

from flask_mail import Message
from pymongo.topology import os

from utils.logger import logger


def send_email(data):
    from run import mail

    logger.info("trying...")
    name = data.get("name")
    email = data.get("email")
    origin = data.get("origin")
    website = data.get("website")
    message = data.get("message")
    recipient = os.environ.get("RECIPIENT")

    subject = f"Message sent from {origin}, by {name}"
    body = f"Sent From: {origin}\nName: {name}\nContact Email: {email}"
    html = f"<h4>Contact message sent from <b>{origin}</b>:</h4>\n\n"
    html = f"{html}<p><b>Name:</b> {name}</p>" f"<p><b>Contact Email:</b> {email}</p>"
    if website:
        body = f"{body}\nWebsite: {website}"
        html = f"{html}<p><b>Website</b>: {website}</p>"
    if message:
        body = f"{body}\nMessage: {message}"
        html = f"{html}<p><b>Message:</b> <i>{message}</i></p>"

    msg = Message(subject=subject, recipients=[recipient])
    msg.body = body
    msg.html = html
    mail.send(msg)

    logger.info("Mail sent... I guess")

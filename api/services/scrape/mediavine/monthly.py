from datetime import date
from .controller import get_mediavine_revenue
from api.models import Database

db = Database()
db.initialize()


def handler():
    ammount: str = get_mediavine_revenue("monthly")

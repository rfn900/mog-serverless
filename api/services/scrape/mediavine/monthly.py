from .controller import get_mediavine_revenue
from api.commissions.model import Commissions

db = Commissions()
db.initialize()


def handler():
    ammount: str = get_mediavine_revenue("monthly")

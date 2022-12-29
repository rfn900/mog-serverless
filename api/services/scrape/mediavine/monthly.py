from .controller import get_mediavine_revenue

# from api.commissions.model import Commissions


def handler():
    ammount: str = get_mediavine_revenue("monthly")

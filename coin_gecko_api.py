from pycoingecko import CoinGeckoAPI
import csv, json, os.path
from loguru import logger

class CoinGecko:

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.cg = CoinGeckoAPI()


cg = CoinGeckoAPI()

def current_price(ids='bitcoin, litecoin, ethereum', vs_currencies='usd'):
    db_data = cg.get_price(ids, vs_currencies)
    return db_data

cp = current_price()
print(cp)
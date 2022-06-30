from Secret import Constants
from binance import Client
from python_bitvavo_api.bitvavo import Bitvavo
from datetime import datetime
client_binance = Client(Constants.api_key_binance, Constants.api_secret_binance)

bitvavo = Bitvavo({
	'APIKEY': Constants.api_key_bitvavo,
	'APISECRET': Constants.api_secret_bitvavo,
	'RESTURL': 'https://api.bitvavo.com/v2',
	'WSURL': 'wss://ws.bitvavo.com/v2/',
	'ACCESSWINDOW': 10000,
	'DEBUGGING': False
})

def balance_binance(symbol: str):
    return float(client_binance.get_asset_balance(asset=symbol)['free'])


def price_binance(coin_pair: str):
    return float(client_binance.get_ticker(symbol=coin_pair)['lastPrice'])


def balance_bitvavo(symbol: str):
	return float(bitvavo.balance({"symbol": str.upper(symbol)})[0]['available'])


def price_bitvavo(symbol: str):
	pair = str.upper(symbol) + '-EUR'
	return float(bitvavo.tickerPrice({"market": pair})['price'])


def log(file: str):
    try:
        f = open(file, "r")
        return (f.read())
    except FileNotFoundError:
        return 'FileNotFound'


def time_format(time):
	s = time.split('.')
	t = datetime.strptime(s[0], "%Y-%m-%d %H:%M:%S")
	return datetime.strftime(t, "%d-%m-%y %H:%M")

def cost(action: str, amount, price):
	if action == 'Sell':
		return 0.0075 * float(amount) * float(price)
	elif action == 'Buy':
		return 0.0075 * float(amount)
	else:
		return 0

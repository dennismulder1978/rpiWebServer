from Secret import Constants
from python_bitvavo_api.bitvavo import Bitvavo
from datetime import datetime

bitvavo = Bitvavo({
    'APIKEY': Constants.api_key_bitvavo,
    'APISECRET': Constants.api_secret_bitvavo,
    'RESTURL': 'https://api.bitvavo.com/v2',
    'WSURL': 'wss://ws.bitvavo.com/v2/',
    'ACCESSWINDOW': 10000,
    'DEBUGGING': False
})


def pos_coin():
    coin_dict_lst = [x for x in bitvavo.balance({}) if float(x['available']) > 0]
    coin_symbol_lst = [y['symbol'] for y in coin_dict_lst]
    try:
        coin_symbol_lst.remove('EUR')
    except Exception as e:
        print(e)
    coin_balance_dict = {}
    for z in coin_dict_lst:
        coin_balance_dict[z['symbol']] = float(z['available'])
    return coin_symbol_lst, coin_balance_dict


def price_bitvavo(symbol: str):
    pair = str.upper(symbol) + '-EUR'
    return float(bitvavo.tickerPrice({"market": pair})['price'])


def log(file: str):
    try:
        f = open(file, "r")
        return f.read()
    except FileNotFoundError as fnf:
        return f'FileNotFound {fnf}'


def time_format(time):
    s = time.split('.')
    t = datetime.strptime(s[0], "%Y-%m-%d %H:%M:%S")
    return datetime.strftime(t, "%d-%m-%y %H:%M")



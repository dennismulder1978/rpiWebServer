from flask import Flask, render_template
from functions import *



#starting the website
app = Flask(__name__)
@app.route("/")
def start():

	# actual prices and balances
#	dollar_euro_price= 1/price_binance('EURBUSD')
#	btc_price = price_binance('BTCBUSD')
#	sol_price = price_binance('SOLBUSD')
#	ada_price = price_binance('ADABUSD')
#	sand_price = price_binance('SANDBUSD')
#	bnb_price = price_binance('BNBBUSD')
	btc_bitvavo_price = price_bitvavo('BTC')
	eth_bitvavo_price = price_bitvavo('ETH')
	ada_bitvavo_price = price_bitvavo('ADA')
	sol_bitvavo_price = price_bitvavo('SOL')

#	btc_bal = balance_binance('BTC')
#	sol_bal = balance_binance('SOL')
#	ada_bal = balance_binance('ADA')
#	sand_bal = balance_binance('SAND')
#	bnb_bal = balance_binance('BNB')
	btc_bitvavo_bal = balance_bitvavo('BTC')
	eth_bitvavo_bal = balance_bitvavo('ETH')
	ada_bitvavo_bal = balance_bitvavo('ADA')
	sol_bitvavo_bal = balance_bitvavo('SOL')
	euro_bitvavo_bal = balance_bitvavo('EUR')

#	BTC = [btc_price, btc_bal]
#	SOL = [sol_price, sol_bal]
#	ADA = [ada_price, ada_bal]
#	SAND = [sand_price, sand_bal]
#	BNB = [bnb_price, bnb_bal]
	BTC_BITVAVO = [btc_bitvavo_price, btc_bitvavo_bal]
	ETH_BITVAVO = [eth_bitvavo_price, eth_bitvavo_bal]
	ADA_BITVAVO = [ada_bitvavo_price, ada_bitvavo_bal]
	SOL_BITVAVO = [sol_bitvavo_price, sol_bitvavo_bal]

#	balance_binance_BUSD = balance_binance('BUSD')
	balance_bitvavo_EURO = balance_bitvavo('EUR')

#	tot_bal_euro = (btc_bal * btc_price) * dollar_euro_price
#	tot_bal_euro += (sol_bal * sol_price) * dollar_euro_price
#	tot_bal_euro += (ada_bal * ada_price) * dollar_euro_price
#	tot_bal_euro += (sand_bal * sand_price) * dollar_euro_price
#	tot_bal_euro += (bnb_bal * bnb_price) * dollar_euro_price
#	tot_bal_euro += balance_binance_BUSD * dollar_euro_price
	tot_bal_euro = (btc_bitvavo_bal * btc_bitvavo_price) + (eth_bitvavo_bal * eth_bitvavo_price) + (ada_bitvavo_bal * ada_bitvavo_price) + (sol_bitvavo_bal * sol_bitvavo_price)
	tot_bal_euro += balance_bitvavo_EURO


	# Historical trade data Binane
#	csv_data_lines = log('/home/pi/multitrade/action.csv').splitlines()[1::]
#	csv_data = [i.split(',') for i in csv_data_lines]
#	BTC_data = [[i[0],i[3],time_format(i[5]), cost(i[0],i[2],i[3])] for i in csv_data if i[1] == "BTCBUSD"][:-20:-1]
#	ADA_data = [[i[0],i[3],time_format(i[5]), cost(i[0],i[2],i[3])] for i in csv_data if i[1] == "ADABUSD"][:-20:-1]
#	SAND_data = [[i[0],i[3],time_format(i[5]), cost(i[0],i[2],i[3])] for i in csv_data if i[1] == "SANDBUSD"][:-20:-1]
#	SOL_data = [[i[0],i[3],time_format(i[5]), cost(i[0],i[2],i[3])] for i in csv_data if i[1] == "SOLBUSD"][:-20:-1]

	# Historical trade data Bitvavo
	csv_data_lines_bitvavo = log('/home/pi/bitvavo/action.csv').splitlines()[1::]
	csv_data_bitvavo = [i.split(',') for i in csv_data_lines_bitvavo]
	bitvavo_data = [[i[0],i[1],i[2],i[3],round((float(i[2])*float(i[3])),2),time_format(i[5]),round((float(i[2])*float(i[3])*0.0025),2)] for i in csv_data_bitvavo][:-100:-1]

	templateData = {
#		'btc_trade_data': BTC_data,
#		'ada_trade_data': ADA_data,
#		'bitvavo_data': bitvavo_data,
#       	        'sand_trade_data': SAND_data,
#               	'sol_trade_data': SOL_data,
#		'balance_binance_BUSD': balance_binance_BUSD,
		'balance_bitvavo_EURO': balance_bitvavo_EURO,
#		'BTC': BTC,
#		'SOL': SOL,
#		'ADA': ADA,
#		'SAND': SAND,
#		'BNB': BNB,
		'BTC_BITVAVO': BTC_BITVAVO,
		'ETH_BITVAVO': ETH_BITVAVO,
		'ADA_BITVAVO': ADA_BITVAVO,
		'SOL_BITVAVO': SOL_BITVAVO,
		'BAL_TOT': tot_bal_euro,
		'BAL_EURO': euro_bitvavo_bal,
#		'dollar_euro_price': dollar_euro_price,
		'bitvavo_data': bitvavo_data,
      	}

	return render_template('index.html', **templateData)


if __name__ == "__main__":
	app.run(host='192.168.0.123', port=80, debug=True)

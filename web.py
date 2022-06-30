from flask import Flask, render_template
from functions import *

# Starting the website
app = Flask(__name__)


@app.route("/")
def start():
    # determine coins, balance and price.
    coin_lst, bal_dict = pos_coin()
    price_dict = {}
    for each in coin_lst:
        if each != 'EUR':
            price_dict[each] = price_bitvavo(each)

    # determine total value
    tot_bal_euro = float(0)
    try:
        tot_bal_euro += bal_dict['EUR']
    except Exception as e:
        print(e)

    for each in coin_lst:
        tot_bal_euro += (bal_dict[each] * price_dict[each])
    tot_bal_euro = round(tot_bal_euro, 2)

    # output test
    print(f'Coin list: {coin_lst}')
    print(f'Balance: {bal_dict}')
    print(f'Price: {price_dict}')
    print(f'Total balance: €{tot_bal_euro}')

    # Historical trade data Bitvavo
    csv_data_lines_bitvavo = log('/home/pi/new_RPI_BITV/rasp_bitvavo/action.csv').splitlines()[1::]
    csv_data_bitvavo = [i.split(',') for i in csv_data_lines_bitvavo]
    bitvavo_data = [[i[0],
                     i[1],
                     i[2],
                     i[3],
                     round((float(i[2]) * float(i[3])), 2),
                     time_format(i[5]),
                     round((float(i[2]) * float(i[3]) * 0.0025), 2)] for i in csv_data_bitvavo][:-100:-1]

    templateData = {
        'balance': bal_dict,
        'price': price_dict,
        'tot_bal_euro': tot_bal_euro,
        'log_data': bitvavo_data,

    }

    return render_template('index.html', **templateData)


if __name__ == "__main__":
    app.run(host='192.168.0.123', port=80, debug=True)

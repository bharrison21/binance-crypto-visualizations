from flask import Flask, json, render_template, request, flash, redirect, jsonify
from flask_cors import CORS
import config, csv
from binance.client import Client
from binance.enums import *



app = Flask(__name__)
CORS(app)

app.secret_key=b'fiasdifhweadfnahf'
client = Client(config.API_KEY,config.API_SECRET, tld='us')


@app.route('/', methods=['POST', 'GET'])
def index():

    title = "Buy The Dip!"
    subtitle="Get Notified of Dips, and when RSI and other factors are encouraging"

    account=client.get_account()
    balances=account['balances']
    exchange_info=client.get_exchange_info()

    symbols=exchange_info['symbols']
    symbols_lst=[]
    for tick in symbols:
        dict_select={}
        dict_select['symbol']=tick['symbol']
        dict_select['selected']=False
        symbols_lst.append(dict_select)

    symbol_select = request.form.get('symbol_select')

    for symbol in symbols_lst:
        selected=''
        if symbol['symbol'] == symbol_select:
            symbol['selected'] == True
            selected+=symbol_select
            break
    processed_candlesticks = []
    candlesticks = client.get_historical_klines(symbol_select, Client.KLINE_INTERVAL_1DAY, "1 JAN, 2021", "10 MAY, 2021")
    for data in candlesticks:
        candlestick= { 
            "time": data[0] / 1000, 
            "open": data[1], 
            "high": data[2], 
            "low": data[3], 
            "close": data[4] 
            }
        processed_candlesticks.append(candlestick) 
    print(selected)
    return render_template('index.html',
    title=title, 
    my_balances=balances, 
    symbols=symbols, 
    subtitle=subtitle, 
    user=processed_candlesticks,
    selected=selected
    )
    
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    # select = request.form.get('symbol_select')
    # processed_candlesticks = []
    # candlesticks = client.get_historical_klines(select, Client.KLINE_INTERVAL_1WEEK, "1 May, 2015", "13 May, 2021")
    # for data in candlesticks:
    #         candlestick= { 
    #             "time": data[0] / 1000, 
    #             "open": data[1], 
    #             "high": data[2], 
    #             "low": data[3], 
    #             "close": data[4] 
    #             }
    #         processed_candlesticks.append(candlestick)     
     
    return jsonify(processed_candlesticks)

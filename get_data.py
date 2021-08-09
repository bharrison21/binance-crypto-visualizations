import config
import csv
from binance.client import Client
from binance import AsyncClient, DepthCacheManager, BinanceSocketManager

client = Client(config.API_KEY,config.API_SECRET)

# prices= client.get_all_tickers()

# for price in prices:
#     print(price)

candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile=open('2015-2020candlesticks.csv', 'w', newline='')
candlestick_writer=csv.writer(csvfile, delimiter=',')


# for candlestick in candles:
#     candlestick_writer.writerow(candlestick)


candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Dec, 2015", "10 May, 2020")

for candle in candlesticks:
    candlestick_writer.writerow(candle)

csvfile.close()
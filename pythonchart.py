import json
import requests
from binance import Client
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
import pandas as pd
import pandas_datareader as pdr
import datetime as dt



symbol = input(F"Enter ticker symbol here: ")
#key = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"

#ticker = "AAPL"
start = dt.datetime(2002, 10, 1)
end = dt.datetime(2002, 10, 8)

data = pdr.get_data_yahoo(symbol, start, end, interval='d')
print(data)

#response = requests.get(key)
#data = response.json()
#print (f"{data} price is {data ['price']}")




#response = 	requests.get("https://cryptingup.com/api/")

#print(response)



# web app with graph or chart that displays current crypto prices
# 


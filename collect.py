#!/usr/bin/python3

import json
import yfinance as yf

# Grab the stocks to check from the "stocks.json" file
stocks_file = open("stocks.json",)
stocks_list = json.load(stocks_file)
stocks_file.close()
stock_names = []
stock_symbols = []
# Extract the stock names and symbols into separate lists
for item in stocks_list['ToCheck']:
    stock_names.append(item)
    stock_symbols.append(stocks_list['ToCheck'][item])

# Grab stock info from each symbol
for item in stock_symbols:
    stock_info = yf.Ticker(item)
    print(stock_info.info)



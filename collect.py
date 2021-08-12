#!/usr/bin/python3

import json
import yfinance as yf

# Grab the stocks to check from the "stocks.json" file
stocks_file = open("stocks.json",'r')
stock_data = json.load(stocks_file)
stocks_file.close()

# Grab stock info from each symbol
for item in stock_data['ToCheck']:
    print("Gathering information on " + item + "...")
    stock_info = yf.Ticker(stock_data['ToCheck'][item])
    stock_data["Info"][item] = stock_info.info

# Write info to json file
stocks_file = open("stocks.json","w")
json.dump(stock_data, stocks_file, indent=4)


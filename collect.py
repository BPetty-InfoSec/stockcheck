import json
import pandas as pd
import numpy as np
import yfinance as yf
from yahoofinancials import YahooFinancials
from datetime import datetime, date, timedelta

ticker = yf.Ticker('AAPL')
aapl_df = ticker.history(period="max")
aapl_df['Close'].plot(title="AAPL's Stock Price")
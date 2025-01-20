import numpy as num
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd

stockdata = yf.download("AAPL TSLA MSFT NVDA GOOG GOOGL", start="2024-01-01", end="2025-01-01")

stockdata['Close'].plot(figsize=(10,5), title="Apple Stock Price")
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.show()

stockdata[['Close', 'SMA50', 'SMA200']].plot(figsize=(10,5), title= "Apple Stock Price with Moving Average")
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.show()

stockdata['Daily Return'].plot(figsize=(10,5), title= "Apple Stock Daily")
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.grid(True)
plt.show()


stockdata['12_EMA'] = stockdata['Close'].ewm(span=12, adjust=False).mean()



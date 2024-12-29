# Import the libraries you will need. Ensure these are installed using pip :)
# To obtain up-to-date, reliable stock data, 'yfinance' is used.
# To frame the necessary data and utilise it, 'Pandas' is used.
# To carry out mathematical calculation, 'NumPy' is used.
# To visualise the data, 'Matplotlib.pyplot' is used.

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Firstly, define the downloaded data and necessary variables. We will use 5 years as a time period
# one day as the interval period.

ticker_symbol = "^GSPC"
start_date = "2019-12-01"
end_date = "2024-12-01"
data = yf.download(tickers=ticker_symbol, start=start_date, end=end_date, interval="1d")

# Define formulae we created earlier needed for plotting (returns, volatility, moving averages)
Daily_Sample = data[( 'Close', '^GSPC')].resample("D").last()
Daily_Returns = np.log(Daily_Sample/ Daily_Sample.shift(1))
Daily_Returns.dropna(inplace=True)

Daily_Volatility = Daily_Returns.rolling(63).std()

SMA_63 = data[( 'Close', '^GSPC')].rolling(window=63).mean()
SMA_63.dropna(inplace=True)


EMA_63 = data[( 'Close', '^GSPC')].ewm(span=63, adjust=False).mean()
EMA_63.dropna(inplace=True)


weights = list(range(1, 64))
WMA_63 = data[( 'Close', '^GSPC')].rolling(window=63).apply(
    lambda prices: np.dot(prices, weights) / sum(weights), raw=True
)
WMA_63.dropna(inplace=True)


# Set the theme and styles using Matplotlib
plt.style.use("seaborn-v0_8-paper")
plt.rc("font", family="serif")

# Because we want to plot the closing prices against volatility, we will need two plots:
fig, axes = plt.subplots(nrows=2, ncols=2, sharex=True, sharey=False)

# Plot the two types of data, setting the colour (etc.) and assigning the subplots.
data[( 'Close', '^GSPC')].plot(ax=axes[0,0], color="purple")
Daily_Volatility.plot(ax=axes[1,1], color="brown")
Daily_Returns.plot(ax=axes[1,0], color="blue")
SMA_63.plot(ax=axes[0,1], color="orange", label="SMA")
EMA_63.plot(ax=axes[0,1], color="green", label="EMA")
WMA_63.plot(ax=axes[0,1], color="red", label="WMA")
data[( 'Close', '^GSPC')].plot(ax=axes[0,1], color="blue", label="Closing Prices, S&P 500")
axes[0,1].legend(loc="upper left")

# Set the appropriate labels for each axes.
axes[0,0].set_title("Closing Prices of the S&P 500", fontsize=7)
axes[0,1].set_title("Moving Averages Visualised Over The Closing Prices", fontsize=7)
axes[1,0].set_title("S&P 500 Returns", fontsize=7)
axes[1,1].set_title("S&P 500 Volatility", fontsize=7)
axes[0,0].set_ylabel("GBP (£)", fontsize=6)
axes[0,1].set_ylabel("GBP (£)", fontsize=6)

# Show in Matplotlib
plt.show()


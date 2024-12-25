# Import the libraries you will need. Ensure these are installed using pip :)
# To obtain up-to-date, reliable stock data, 'yfinance' is used.
# To carry out mathematical calculation, 'NumPy' is used.
import yfinance as yf
import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import adfuller

# Firstly, define the downloaded data and necessary variables. We will use 5 years as a time period and one day as an interval period.
ticker_symbol = "^GSPC"
start_date = "2019-12-01"
end_date = "2024-12-01"
data = yf.download(tickers=ticker_symbol, start=start_date, end=end_date, interval="1d")

# yfinance already produces cleaned data, so there is no need to clean anything here. But for demonstrative purposes, I will do it any ways. I'm going to check for missing values and duplicates:
print(data.isnull().sum())
print(data.duplicated().sum())

# If there were missing or duplicates, you can either: data.dropna(inplace=True) or data.ffill(inplace=True). Given our interval, we use these functions to obtain summary information:
print(data)
print(data.describe())

# Do a stationary test beforehand - Augumented Dickey-Fuller:

adf = adfuller(data[( 'Close', '^GSPC')])
print("ADF Statistic:", adf[0])
print("p value:", adf[1])
print("Critical Values:", adf[4])

if adf[1] < 0.05:
    print("Reject the null hypothesis: The series is stationary.")
else:
    print("Fail to reject the null hypothesis: The series is non-stationary.")

# Our raw data is non-stationary, but since we are using logarithmically transformed variables the data will become transformed. This is common practice in Quantitative Finance.

# Calculate logarithmic returns

Daily_Sample = data[( 'Close', '^GSPC')].resample("D").last()
Daily_Returns = np.log(Daily_Sample/ Daily_Sample.shift(1))
Daily_Returns.dropna(inplace=True)
print(Daily_Returns)


Weekly_Sample = data[( 'Close', '^GSPC')].resample("W").last()
Weekly_Returns = np.log(Weekly_Sample/ Weekly_Sample.shift(1))
Weekly_Returns.dropna(inplace=True)
print(Weekly_Returns)


Yearly_Sample = data[( 'Close', '^GSPC')].resample("YE").last()
Yearly_Returns = np.log(Yearly_Sample/ Yearly_Sample.shift(1))
Yearly_Returns.dropna(inplace=True)
print(Yearly_Returns)

# Calculate raw daily volatility of the start and end of our time period using a 63-day rolling window.

Daily_Volatility = Daily_Returns.rolling(63).std()
Daily_Volatility.dropna(inplace=True)
print(Daily_Volatility)

# Calculate your moving averages over 63-day period:

SMA_63 = data[( 'Close', '^GSPC')].rolling(window=63).mean()
SMA_63.dropna(inplace=True)
print(SMA_63)

EMA_63 = data[( 'Close', '^GSPC')].ewm(span=63, adjust=False).mean()
EMA_63.dropna(inplace=True)
print(EMA_63)

weights = list(range(1, 64))
WMA_63 = data[( 'Close', '^GSPC')].rolling(window=63).apply(
    lambda prices: np.dot(prices, weights) / sum(weights), raw=True
)
WMA_63.dropna(inplace=True)
print(WMA_63)






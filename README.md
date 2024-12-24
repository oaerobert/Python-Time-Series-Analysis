## Time Series Analysis of the S&P 500 Index. 🎃

Languages and Libraries: `Python`🐍 (`Matplotlib`, `Pandas`, `NumPy`) 

Hey! 👋🏾 

This project will analyse the **S&P 500** data, forecast future trends and apply quantitative techniques to evaluate trading strategies.
This is useful for financial forecasting, portfolio management and also, risk assessment.
Below, I've outlined the steps of this project. The workflow and folders are towards the end, hope you enjoy reading :)


---

### 1. Data Acquisition and Preprocessing: 🤏
*Skills: API Integration, Data Handling, Handling of Messy Data, Data Modelling Preparation, Statistical Testing*

- In this project, data will be obtained from the API `yfinance`. You can find relevant stock data from various time frames, and it is widely available for anybody to use.
- A **summary** will be produced using `Pandas`, where you can observe the head of the dataset, it's time range and any relevant variables.
- Any missing values, outliers and anomalies will be handled through **transformations** (e.g., logarithmic returns).
- Various returns will be calculated using `Pandas` for e.g.: daily/weekly/monthly and visualised through `Matplotlib`.
- This will similarly be replicated for rolling averages, volatility and lagged values with the same libraries.
- Then, I shall perform a **stationarity** test (Augmented Dickey-Fuller) to ensure stationarity.

### 2. Exploratory Data Analysis 🫣
*Skills: Data Visualisation, Insight Extraction*

- Here, I will create time series plots of stock prices, their returns and key features. Correlation heatmaps of the variables will also be produced.
- This time series will furthermore be decomposed into trends, seasonalities and residuals using libraries such as `statsmodels`.
- Rolling standard deviations and periods of low and high volatility can be calculated using `Numpy` and visualised using `Matplotlib`

### 3. Time series modelling.
*Skills: Statistical Modelling, Predictive Analysis*

- I will use ARIMA for mean forecasting and GARCH for volatility. I'll do model fitting and parameter tuning, alongside calculating diagnostics such as **ACF, PACF plots and residual analysis**
- **Mean Squared Errors, Mean Absolute Errors and R-Squared** values will be calculated. As studied within my Econometric classes, these metrics are used to evaluate model fit.
- I will compare models and explain their results.



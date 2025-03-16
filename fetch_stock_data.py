import yfinance as yf

# Set the ticker symbol 
ticker_symbol = "AAPL"

# Create a Ticker object for the stock
stock_data = yf.Ticker(ticker_symbol)

# Get historical market data for the past 5 days 
historical_data = stock_data.history(period="5d")

# print the historical data
print("past 5 days Historical data for: ", ticker_symbol)
print(historical_data)

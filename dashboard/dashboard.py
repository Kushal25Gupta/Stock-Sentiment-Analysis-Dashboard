"""
File: dashboard.py
Purpose: Provide an interactive dashboard to display stock data and news sentiment analysis,
         with a refresh button that limits news updates to two per day.
Author: Triumph Kia Teh
Date: 2025-03-17
Description:
    - Allows the user to choose a stock ticker from a list.
    - Dynamically fetches historical stock data for the selected ticker using yfinance.
    - Loads news sentiment data from CSV.
    - Includes a refresh button to update the news data via the news_update module,
      enforcing a maximum of 2 refreshes per day.
    - Displays the last update timestamp for the news data.
Usage:
    Run the dashboard with:
        streamlit run dashboard/dashboard.py
Dependencies:
    - streamlit
    - pandas
    - yfinance
    - transformers
    - python-dotenv
"""

import sys
import os
from datetime import datetime
import streamlit as st
import pandas as pd
import yfinance as yf

# Add the scripts folder to sys.path to import the news_update module
sys.path.append(os.path.join(os.getcwd(), "scripts"))
from news_update import update_news_data

# Set up page configuration
st.set_page_config(page_title="Stock Sentiment Analysis Dashboard", layout="wide")

# Title and description
st.title("Stock Sentiment Analysis Dashboard")
st.markdown("This dashboard displays historical stock data and news sentiment analysis results.")

# --- Sidebar: Stock Ticker Selection ---
st.sidebar.header("Select Stock Ticker")
ticker_options = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
selected_ticker = st.sidebar.selectbox("Stock Ticker", ticker_options)

# --- Fetch Stock Data Dynamically ---
try:
    stock = yf.Ticker(selected_ticker)
    stock_data = stock.history(period="5d")
    stock_data.reset_index(inplace=True)
except Exception as e:
    st.error("Error fetching stock data: " + str(e))
    st.stop()

# --- Sidebar: Date Filter for Stock Data ---
st.sidebar.header("Filter Stock Data by Date")
min_date = stock_data["Date"].min().date()
max_date = stock_data["Date"].max().date()
selected_date = st.sidebar.date_input("Select Date", value=max_date, min_value=min_date, max_value=max_date)
filtered_stock = stock_data[stock_data["Date"].dt.date == selected_date]

st.header(f"Stock Data for {selected_ticker}")
if not filtered_stock.empty:
    st.dataframe(filtered_stock)
else:
    st.write("No stock data available for the selected date.")

# --- Display Stock Price Trend Chart ---
if "Close" in stock_data.columns:
    st.header(f"{selected_ticker} Stock Close Price Trend")
    stock_data_sorted = stock_data.sort_values(by="Date")
    st.line_chart(stock_data_sorted.set_index("Date")["Close"])

# --- Load News Sentiment Data ---
try:
    news_data = pd.read_csv("data/integrated_news_data.csv")
except FileNotFoundError:
    st.error("News sentiment data file not found. Please run the integrated data script first.")
    st.stop()

# --- Sidebar: News Sentiment Refresh Button ---
if st.sidebar.button("Refresh News Data"):
    def handle_news_refresh():
        """
        Handles news data refresh by checking the update info and allowing a maximum of 2 refreshes per day.
        """
        info_file = "data/news_update_info.txt"
        allow_update = False
        refresh_count = 0
        today = datetime.now().date()

        # Check if the info file exists and read last update info
        if os.path.exists(info_file):
            with open(info_file, "r") as f:
                lines = f.readlines()
            if len(lines) >= 2:
                last_update_str = lines[0].strip()
                try:
                    last_update = datetime.strptime(last_update_str, "%Y-%m-%d %H:%M:%S").date()
                except:
                    last_update = None
                try:
                    refresh_count = int(lines[1].strip())
                except:
                    refresh_count = 0
                if last_update == today:
                    if refresh_count < 2:
                        allow_update = True
                    else:
                        allow_update = False
                else:
                    allow_update = True
                    refresh_count = 0
            else:
                allow_update = True
        else:
            allow_update = True

        if allow_update:
            success = update_news_data()
            if success:
                st.success("News data updated successfully!")
            else:
                st.error("Failed to update news data.")
        else:
            st.warning("Maximum news refreshes reached for today. Please try again tomorrow.")

    handle_news_refresh()

# --- Sidebar: News Sentiment Filter ---
st.sidebar.header("Filter News Sentiment")
sentiment_options = news_data["sentiment_label"].unique().tolist() if not news_data.empty else []
selected_sentiment = st.sidebar.selectbox("Select Sentiment", options=["All"] + sentiment_options)

if selected_sentiment != "All":
    filtered_news = news_data[news_data["sentiment_label"] == selected_sentiment]
else:
    filtered_news = news_data

st.header("News Sentiment Analysis")
if not filtered_news.empty:
    st.dataframe(filtered_news)
else:
    st.write("No news sentiment data available for the selected filter.")

# --- Display Last Updated Timestamp for News Data ---
info_file = "data/news_update_info.txt"
if os.path.exists(info_file):
    with open(info_file, "r") as f:
        lines = f.readlines()
    if len(lines) >= 1:
        last_update_str = lines[0].strip()
        st.markdown(f"**News Data Last Updated:** {last_update_str}")

# --- Disclaimer ---
st.markdown("""
> **Disclaimer:** This project is for educational purposes only. Stock data is provided by yfinance and news headlines are sourced via NewsAPI. 
> Data is updated periodically and should not be used as investment advice.
""")

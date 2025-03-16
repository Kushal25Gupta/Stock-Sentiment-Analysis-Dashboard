"""
File: dashboard.py
Purpose: Provide a simple interactive dashboard to display stock data and news sentiment analysis.
Author: Triumph Kia Teh
Date: 2025-03-15
Description:
    - Loads stock data and news sentiment data from CSV files.
    - Displays data in interactive tables and simple visualizations using Streamlit.
Usage:
    Run the dashboard with:
        streamlit run dashboard.py
Dependencies:
    - streamlit
    - pandas
"""
import streamlit as st
import pandas as pd

# Configure the webpage
st.set_page_config(page_title="Stock Sentiment Analysis Dashboard", layout="wide")

# Title of the Dashboard 
st.title("Stock Sentiment Analysis Dashboard")

# Load stock data 
try:
    stock_data = pd.read_csv("integrated_stock_data.csv")
except FileNotFoundError:
    st.error("Stock data file not found. Please run the data ingestion script first")

# # Load news sentiment data
try:
    news_data = pd.read_csv("integrated_news_data.csv")
except FileNotFoundError:
    st.error("News sentiment data file not found. Please run the data ingestion script first.")

# Display the data 
st.header("Stock Data (Latest)")
if not stock_data.empty:
    st.dataframe(stock_data.head()) # display first few rows of the DataFrame in an interactive table
else:
    st.write("No stock data available.")

st.header("News Sentiment Analysis (Latest)")
if not news_data.empty:
    st.dataframe(news_data.head())
else: 
    st.write("No news sentiment data available.")

# Add a simple chart for stock close prices (if available)
if "Close" in stock_data.columns:
    st.header("Stock Close Price Trend")
    st.line_chart(stock_data["Close"])
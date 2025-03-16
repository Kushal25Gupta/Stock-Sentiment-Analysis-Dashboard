"""
File: integrated_data.py
Purpose: Integrates stock data and news sentiment analysis by fetching historical stock data using yfinance and top news headlines via NewsAPI. 
         It then applies sentiment analysis on the news headlines using Hugging Face's transformers pipeline, and outputs the results.
Author: Triumph Kia Teh
Date: 2025-03-15
Time: 01:30 AM
Description:
    - Part 1: Fetches historical stock data for a specified ticker (default is AAPL).
    - Part 2: Retrieves top US news headlines and analyzes their sentiment.
    - Part 3: Combines and displays the data, and saves the output to CSV files for further analysis.
Usage:
    Run the script with:
        python integrated_data.py
Dependencies:
    - yfinance
    - requests
    - transformers
    - pandas
    - python-dotenv
"""
import os
from dotenv import load_dotenv
import yfinance as yf
import requests 
from transformers import pipeline
import pandas as pd

#-----------------------------------------------------------
# load environment variables from the .env file 
load_dotenv()

#-----------------------------------------------------------
# Part1: Fetch Stock Data 
#-----------------------------------------------------------
ticker_symbol = "AAPL" # can change to other stocks symbol
stock = yf.Ticker(ticker_symbol) # create Ticker object 'stock' which has methods that allow us to retrieve stock data
stock_data = stock.history(period="5d")
# Convert index (date) to column
stock_data.reset_index(inplace=True)  # pandas DataFrame now uses a simple integer index

#-----------------------------------------------------------
# Part 2: Fetch New Headlines and Analyze Their Sentiment
#-----------------------------------------------------------
# Retrieve my news API key from the environment (from .env file)
news_api_key = os.environ.get("NEWSAPI_KEY")

# Set up the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# URL to fetch top US headlines 
news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"
news_response = requests.get(news_url)
news_data = news_response.json()

# Check if the news API request was successful 
if news_data.get("status") != "ok":
    print("Failed to fetch news data:", news_data)
    exit()  # terminates execution of this Python script, preventing any further code from running on bad data.

# Process each news article: get headline and its sentiment 
news_list = []
for article in news_data.get("articles", []):
    headline = article.get("title", "No Title")
    sentiment = sentiment_pipeline(headline)[0] # get first result (which is the dictionary of label and score for this article)
    news_list.append({
        "headline": headline, 
        "sentiment_label": sentiment["label"],  # get sentiment (the value of the key 'label')
        "sentiment_score": sentiment["score"],  # get confidence score (the value of the key 'score')
    })

# Convert news_list to a pandas DataFrame
news_df = pd.DataFrame(news_list)

#-----------------------------------------------------------
# Part 3: Combine and Display Stock + News Data 
#-----------------------------------------------------------
# For demonstration, display on first few rows 
# Also, save both data to CSV files for later analysis
print("Stock Data (First Few Rows):")
print(stock_data.head())

print("\nNews Data with Sentiment (First Few Rows):")
print(news_df.head())

# Save outputs to CSV files 
stock_data.to_csv("integrated_stock_data.csv", index=False)
news_df.to_csv("integrated_news_data.csv", index=False)

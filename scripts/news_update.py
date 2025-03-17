"""
File: news_update.py
Purpose: Fetches financial news from NewsAPI, performs sentiment analysis using Hugging Face's pipeline,
         saves the results to a CSV, and records the update timestamp and refresh count.
Author: Triumph Kia Teh
Date: 2025-03-17
Usage:
    This module defines a function `update_news_data()` that can be called to update the news data.
Dependencies:
    - requests
    - pandas
    - transformers
    - python-dotenv
    - datetime
"""

import os
import requests
import pandas as pd
from transformers import pipeline
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def update_news_data():
    """
    Fetches news headlines using NewsAPI, performs sentiment analysis, and saves results to CSV.
    Also writes the current timestamp and refresh count to a tracking file.
    Returns True on success, False otherwise.
    """
    news_api_key = os.environ.get("NEWSAPI_KEY")
    if not news_api_key:
        print("NEWSAPI_KEY not set in .env")
        return False

    news_url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"
    response = requests.get(news_url)
    news_data = response.json()

    if news_data.get("status") != "ok":
        print("Error fetching news data:", news_data)
        return False

    # Set up sentiment analysis pipeline
    sentiment_pipeline = pipeline("sentiment-analysis")
    
    # Process each article to get sentiment information
    news_list = []
    for article in news_data.get("articles", []):
        headline = article.get("title", "No Title")
        try:
            sentiment = sentiment_pipeline(headline)[0]
        except Exception as e:
            sentiment = {"label": "UNKNOWN", "score": 0.0}
        news_list.append({
            "headline": headline,
            "sentiment_label": sentiment["label"],
            "sentiment_score": sentiment["score"],
        })

    # Convert list to DataFrame and save to CSV
    news_df = pd.DataFrame(news_list)
    csv_path = "data/integrated_news_data.csv"
    try:
        news_df.to_csv(csv_path, index=False)
    except Exception as e:
        print("Error saving CSV:", e)
        return False

    # Write/update news update info file (timestamp and refresh count)
    info_file = "data/news_update_info.txt"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # If info file exists and is from today, increment the count; otherwise, reset to 1.
    refresh_count = 1
    if os.path.exists(info_file):
        with open(info_file, "r") as f:
            lines = f.readlines()
        if len(lines) >= 2:
            last_update_str = lines[0].strip()
            try:
                last_update = datetime.strptime(last_update_str, "%Y-%m-%d %H:%M:%S")
                if last_update.date() == datetime.now().date():
                    # Increment refresh count if already updated today
                    try:
                        refresh_count = int(lines[1].strip()) + 1
                    except:
                        refresh_count = 1
            except Exception as e:
                refresh_count = 1

    with open(info_file, "w") as f:
        f.write(f"{current_time}\n{refresh_count}")

    print("News data updated successfully at", current_time, "with refresh count:", refresh_count)
    return True

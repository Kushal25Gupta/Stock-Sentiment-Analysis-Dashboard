import os
from dotenv import load_dotenv
import requests       # to fetch data
from transformers import pipeline     # for sentiment analysis

# ---------------------------------------------------------
# Load environment variables from the .env file
load_dotenv()

# ---------------------------------------------------------
# Fetch News Headlines and Analyze Their Sentiment
# ---------------------------------------------------------

# Retrieve the API key from the environment (from .env file)
news_api_key = os.environ.get("NEWSAPI_KEY")

# Set up the sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# URL to fetch top US headlines (can change 'us' to another country code if you wish)
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api_key}"

# Make a GET request to fetch the news data
response = requests.get(url)
news_data = response.json()  # == dictionary of headline data 

# Check if the request was successful
if news_data.get("status") != "ok":
    print("Failed to fetch news data:", news_data)
    exit()

# Check how many headlines are in news_data
print("\nNumber of headlines:", len(news_data.get("articles", [])))

# Loop through each article and analyze its headline sentiment
print("News Headlines and Their Sentiments Analysis:\n")
for article in news_data.get("articles", []):
    headline = article.get("title", "No Title")
    sentiment = sentiment_pipeline(headline)
    print(f"Headline: {headline}")
    print(f"Sentiment: {sentiment}\n")

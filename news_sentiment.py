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
news_data = response.json()  # dictionary of headline data

# Prepare a list to store output lines
output_lines = []

# Check if the request was successful
if news_data.get("status") != "ok":
    error_message = f"Failed to fetch news data: {news_data}"
    output_lines.append(error_message)
    print(error_message)
    exit()

# Add number of headlines to output
num_headlines = len(news_data.get("articles", []))
output_lines.append(f"\nNumber of headlines: {num_headlines}")

# Add header line for clarity
output_lines.append("News Headlines and Their Sentiments Analysis:\n")

# Loop through each article and analyze its headline sentiment
for article in news_data.get("articles", []):
    headline = article.get("title", "No Title")
    sentiment = sentiment_pipeline(headline)
    output_lines.append(f"Headline: {headline}")
    output_lines.append(f"Sentiment: {sentiment}\n")

# Write the output to a file
with open("sentiment_output.txt", "w") as file:
    file.write("\n".join(output_lines))

# Optionally, print the output to the console
print("\n".join(output_lines))

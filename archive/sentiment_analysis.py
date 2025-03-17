# Import the pipeline function from the transformers library.
from transformers import pipeline

# Create a sentiment analysis pipeline using a pre-trained model 
# (default is usually a model like 'distilbert-base-uncased-finetuned-sst-2-english')
sentiment_pipeline = pipeline("sentiment-analysis")

# Customizable text for sentiment analysis
example_text = "The market is looking very promising today!"

# performing sentiment analysis on example_text
sentiment = sentiment_pipeline(example_text)

# print the sentiment 
print("Sentiment analysis result:")
print(sentiment)
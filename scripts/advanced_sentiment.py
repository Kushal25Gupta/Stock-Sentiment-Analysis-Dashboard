"""
File: advanced_sentiment.py
Purpose: Explore advanced NLP techniques on financial news headlines.
         Currently, it uses a pre-trained emotion detection model to capture a range of emotions.
         Future enhancements will include fine-tuning and aspect-based sentiment analysis.
Author: Triumph Kia Teh
Date: 2025-03-16
Description:
    - Loads a list of example financial news headlines.
    - Uses a pre-trained emotion detection model from Hugging Face.
    - Prints the detected emotions for each headline.
Usage:
    Run the script with:
        python scripts/advanced_sentiment.py
Dependencies:
    - transformers
    - python-dotenv (if API keys are needed later)
"""
from transformers import pipeline

# Set up an emotion dectection pipeline using a Hugging Face Model. 
# This model ("nateraw/bert-base-uncased-emotion") detects emotions such as anger, joy, sadness, etc.
emotion_pipeline = pipeline("text-classification", model="nateraw/bert-base-uncased-emotion")

# Example headlines - In practice, you could fetch these from your NewsAPI.
headlines = [
    "Apple posts record revenue amid strong iPhone sales",
    "Market crashes as investors panic over global tensions",
    "Tech giants show renewed optimism for future growth",
    "Economic slowdown raises concerns among industry experts"
]

# Process each headline and detect emotions. 
for headline in headlines:
    emotions = emotion_pipeline(headline)
    print(f"Headline:{headline}")
    print("Detected Emotions:")
    for result in emotions:
        # print the label and score from the result dictionary in a nicely formatted way. 
        print(f"  - {result['label']}: {result['score']:.3f}")
    print("\n")

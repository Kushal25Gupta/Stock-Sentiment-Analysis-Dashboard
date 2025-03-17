# Project Roadmap: Stock Sentiment Analysis MVP

## Overview
The **Stock Sentiment Analysis App** is a Python-based MVP that integrates real-time stock data with basic sentiment analysis of financial news headlines. The project fetches historical stock data using yfinance, retrieves financial news via NewsAPI, and uses a pre-trained transformer pipeline for sentiment analysis. The results are saved into CSV files and visualized using a simple interactive dashboard built with Streamlit.

## Key Features
- **Real-Time Data Ingestion:**
  - Fetch stock data using [yfinance](https://pypi.org/project/yfinance/).
  - Retrieve financial news headlines via [NewsAPI](https://newsapi.org/).

- **Basic Sentiment Analysis:**
  - Use a pre-trained transformer pipeline (e.g., DistilBERT) from Hugging Face for sentiment analysis on news headlines.

- **Data Integration:**
  - Combine stock data and sentiment analysis results using Pandas.
  - Save the processed data to CSV files for further analysis.

- **Interactive Dashboard:**
  - Display the integrated data using a simple Streamlit dashboard.

- **Version Control & Documentation:**
  - Utilize Git & GitHub for version control, following best practices with feature branching and thorough documentation.

## Timeline & Milestones
- **Milestone 1:** Data Ingestion & Basic Sentiment Analysis (Completed)
- **Milestone 2:** Data Integration & Output Storage (Completed)
- **Milestone 3:** Develop and Launch the Simple Interactive Dashboard (In Progress/Completed)

## Future Enhancements (For Future Projects)
- Advanced NLP techniques (fine-tuning, aspect-based analysis, emotion detection)
- Deep Learning Prediction Models
- Distributed Streaming & Database Integration
- Full-Stack Web Application with modern frameworks (React, Node.js/Django, HTML, CSS)
- Containerization, CI/CD, and Cloud Deployment
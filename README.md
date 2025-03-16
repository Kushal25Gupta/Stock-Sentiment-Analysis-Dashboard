# Stock Sentiment Analysis App

## Overview
The **Stock Sentiment Analysis App** is a Python-based project that integrates real-time stock data with advanced NLP techniques to analyze financial news and predict stock market movements. It demonstrates state-of-the-art data ingestion, sentiment analysis, deep learning prediction, and follows industry best practices such as containerization and deployment.

## Key Features
- **Real-Time Data Ingestion**  
  - Fetch live stock data using [yfinance](https://pypi.org/project/yfinance/).  
  - Retrieve financial news headlines via [NewsAPI](https://newsapi.org/).  

- **Advanced NLP Techniques**  
  - **Fine-Tuning**: Train or fine-tune transformer models (e.g., BERT) for domain-specific sentiment analysis.  
  - **Aspect-Based Sentiment Analysis**: Drill down into headlines for sentiments on earnings, management, etc.  
  - **Emotion Detection**: Go beyond positive/negative to detect a range of emotions in news articles.  

- **Deep Learning Prediction**  
  - Utilize an LSTM model to forecast stock price movements from historical data.

- **Interactive Dashboard**  
  - (Planned) Build a real-time web interface (using Streamlit or React) to visualize data, sentiment, and predictions.

- **Distributed Streaming & Database Integration**  
  - (Planned) Incorporate Kafka or AWS Kinesis for streaming.  
  - Use SQL/NoSQL (e.g., PostgreSQL or MongoDB) for data storage and querying.

- **Automation & Deployment**  
  - (Planned) Automate data pipelines with Airflow or Prefect.  
  - Containerize with Docker and orchestrate using Kubernetes.

## Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Triumph-KT/Stock-Sentiment-Analysis-App.git
   cd Stock-Sentiment-Analysis-App
   ```

2. **Create and Activate a Virtual Environment (Recommended)**  
   ```bash
   # Create a virtual environment named "venv"
   python -m venv venv

   # Activate it on macOS/Linux
   source venv/bin/activate

   # On Windows
   # venv\Scripts\activate
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
   *If no `requirements.txt` is present, install packages individually:*  
   ```bash
   pip install yfinance requests transformers pandas python-dotenv
   ```

   **For Advanced Features:**  
   If using deep learning models (LSTM), install:
   ```bash
   pip install tensorflow keras
   ```
   If fine-tuning NLP models, install:
   ```bash
   pip install datasets transformers torch
   ```

4. **Set Up Environment Variables**  
   - Create a file named `.env` in the root directory of this project.
   - Add your NewsAPI key (replace `your_actual_newsapi_key` with your own key):  
     ```ini
     NEWSAPI_KEY=your_actual_newsapi_key
     ```
   - Any other environment variables can be added here as needed.

## Usage

1. **Fetch News and Perform Sentiment Analysis**  
   ```bash
   python news_sentiment.py
   ```
   This script retrieves the latest news headlines from NewsAPI and uses a transformer-based model to analyze sentiment.

2. **Fetch Stock Data and Integrate With News**  
   ```bash
   python integrated_data.py
   ```
   This script fetches historical stock data (default: AAPL) and combines it with news sentiment results for further analysis.

3. **Run Advanced Scripts (Planned)**  
   - **Fine-Tuning**: A script for fine-tuning BERT on a domain-specific dataset.  
   - **Aspect-Based**: A script focusing on extracting and analyzing particular financial aspects.  
   - **LSTM Prediction**: A script to train and run LSTM-based stock price predictions.  

   *(These advanced features are in development.)*

## Expected Output Examples

- **Sentiment Analysis Result:**  
  ```json
  [
    {
      "headline": "Apple reports record revenue in Q1",
      "sentiment_label": "POSITIVE",
      "sentiment_score": 0.98
    }
  ]
  ```

- **Stock Price Prediction (Future LSTM Model):**  
  ```json
  {
    "Date": "2025-03-15",
    "Predicted_Close_Price": 225.45
  }
  ```

## Project Roadmap
For more detailed information about planned features and future milestones, refer to the `PROJECT_ROADMAP.md` file. It outlines the overall vision, feature list, and timeline for the project.

## Contributing
1. Fork the repository.  
2. Create a new branch.  
3. Make changes, commit, and push.  
4. Open a pull request describing your changes.

## License
This project is open source under the MIT License.  
Feel free to modify and use it for your own applications.
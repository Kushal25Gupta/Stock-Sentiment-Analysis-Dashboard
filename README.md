# Stock Sentiment Analysis Dashboard

## Overview
The Stock Sentiment Analysis Dashboard is a Python-based MVP that integrates real-time stock data with basic sentiment analysis of financial news headlines. The project fetches historical stock data using yfinance, retrieves news headlines via NewsAPI, performs sentiment analysis using Hugging Face's transformers pipeline, and saves the results into CSV files. A simple Streamlit dashboard is provided to visualize the data.

## Key Features
- **Real-Time Data Ingestion**  
  - Fetch live stock data using [yfinance](https://pypi.org/project/yfinance/).  
  - Retrieve financial news headlines via [NewsAPI](https://newsapi.org/).

- **Real-Time Data Ingestion:** Fetch historical stock data using yfinance and financial news headlines via NewsAPI.
- **Sentiment Analysis:** Perform sentiment analysis on news headlines using Hugging Face's transformers pipeline.
- **Data Integration:** Combine and save the results into CSV files.
- **Interactive Dashboard:** View the processed data in a simple, interactive dashboard built with Streamlit.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Triumph-KT/Stock-Sentiment-Analysis-App.git
   cd Stock-Sentiment-Analysis-App


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
   - Add your NewsAPI key (replace `your_actual_newsapi_key` with your key):
     ```ini
     NEWSAPI_KEY=your_actual_newsapi_key
     ```
   - Add any other environment variables as needed.

## Usage

1. **Fetch Stock Data and Integrate with News**  
   ```bash
   python integrated_data.py
   ```
   This script fetches historical stock data (default: AAPL) using yfinance, integrates it with news sentiment analysis, and saves the combined results to CSV files.

2. **View the Dashboard**  
   Launch the Streamlit dashboard to visualize the data.
   ```bash
   streamlit run dashboard/dashboard.py
   ```

## Demo

![Dashboard Screenshot](docs/screenshot-dashboard.png)

*(Place the screenshot image in a folder like `docs/` or `images/` in your project.)*

## Future Enhancements

- Integrate advanced NLP techniques such as fine-tuning and aspect-based sentiment analysis.
- Develop a deep learning model for stock price prediction.
- Evolve the dashboard into a full-stack web application using React and Django/Node.js.

## Contributing
1. Fork the repository.  
2. Create a new branch for your feature or bug fix.  
3. Make your changes, commit, and push them.  
4. Open a pull request describing your changes.

## License
This project is open source under the [MIT License](LICENSE). Feel free to modify and use it for your own applications.

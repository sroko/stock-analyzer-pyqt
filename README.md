Stock Trend Analyzer

A lightweight desktop application built with Python and PyQt5 that allows users to analyze stock market trends in real-time using the Yahoo Finance API.
Features:
    - Real-time Analysis: Fetches live historical stock data for any valid ticker.
    - Technical Indicators: Automatically calculates and visualizes SMA 50 (50-day Simple Moving Average) and SMA 200 (200-day Simple Moving Average) to help identify market trends.
    - User-Friendly Interface: Built with PyQt5, featuring an interactive date picker for custom analysis ranges.
    - Robust Error Handling: Built-in alerts to notify users of invalid tickers or missing data.

INSTALLATION AND USAGE
Clone the repository:
    git clone https://github.com/sroko/stock-analyzer-pyqt.git
    cd stock-analyzer-pyqt

Install dependencies
    pip install PyQt5 matplotlib yfinance

Run
    python main.py

License
    This project is licensed under the MIT License.
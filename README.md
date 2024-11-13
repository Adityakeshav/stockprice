
# Stock Price Data Web App

A simple and interactive Streamlit app that fetches and visualizes stock price data using the `yfinance` library. The app allows users to input a stock ticker and date range to view stock data, along with visualizations for the closing price and volume.

## Features
- **Stock Ticker Input**: Enter any stock ticker (e.g., AAPL, TSLA, GOOG) to retrieve the data.
- **Date Range Selector**: Choose the start and end dates for the stock data.
- **Data Visualizations**: View line charts for stock closing prices and bar charts for stock trading volume over the selected period.

## Installation

To run the app locally, follow these steps:

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/stock-price-data-web-app.git
cd stock-price-data-web-app
```

### 2. Install dependencies:
```bash
pip install streamlit yfinance pandas
```

### 3. Run the app:
```bash
streamlit run app.py
```

The app will open in your default web browser, and you can start exploring stock data and visualizations.

## Access the Deployed App

You can access the app online at the following links:

- **Streamlit Deployment**: [https://astockprice.streamlit.app/](https://astockprice.streamlit.app/)
- **Azure Deployment**: [https://stockprice-f7h3abc3cwghf5fw.centralindia-01.azurewebsites.net/](https://stockprice-f7h3abc3cwghf5fw.centralindia-01.azurewebsites.net/)

## Technologies Used
- **Streamlit**: For building the interactive user interface.
- **yfinance**: To fetch historical stock data.
- **Pandas**: For data manipulation and processing.

## Contributing
Feel free to fork the repository and submit pull requests. If you have any suggestions or issues, open an issue on GitHub.


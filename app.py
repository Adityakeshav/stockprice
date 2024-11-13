import yfinance as yf
import streamlit as st
import pandas as pd

st.title("Stock Price Data-Driven Web App")
st.write("This web app fetches stock price data and visualizes it.")

# Sidebar for user input
ticker_symbol = st.sidebar.text_input("Enter Stock Ticker Symbol", "AAPL")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2023-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

@st.cache_data
def load_data(ticker, start, end):
    try:
        stock_data = yf.download(ticker, start=start, end=end)
        return stock_data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

if ticker_symbol:
    data = load_data(ticker_symbol, start_date, end_date)
    if data is not None and not data.empty:
        # Display raw data
        st.write(f"Displaying stock data for {ticker_symbol}")
        st.dataframe(data.tail())

        # Plot stock closing price
        st.subheader(f"{ticker_symbol} Closing Price")
        st.line_chart(data['Close'])

        # Plot stock volume
        st.subheader(f'{ticker_symbol} Volume')
        st.line_chart(data['Volume'])
    else:
        st.error("No data found for the given ticker symbol and date range.")
else:
    st.info("Please enter a stock ticker symbol to fetch data.")
import yfinance as yf
import streamlit as st
import pandas as pd

st.title("Stock Price Data-Driven Web App")
st.write("This web app fetch stock price data and visualize it.")

#sidebar for user input
ticker_symbol=st.sidebar.text_input("Enter Stock Ticker Symbol","AAPL")
start_date=st.sidebar.date_input("Start Date",pd.to_datetime("2023-01-01"))
end_date=st.sidebar.date_input("End Date",pd.to_datetime("today"))
try:
    #fetch stock data from yahoo Finanace
    @st.cache_data
    def load_data(ticker,start,end):
        stock_data=yf.download(ticker,start=start,end=end)
        return stock_data
    if ticker_symbol:
        data=load_data(ticker_symbol,start_date,end_date)

        #display raw data
        st.write(f"Displaying stock data for {ticker_symbol}")
        st.dataframe(data.tail())
        #plot stock closing price
        st.subheader(f"{ticker_symbol} Closing Price")
        st.line_chart(data['Close'])

        #plot stock volume
        st.subheader(f'{ticker_symbol} Volume')
        st.line_chart(data['Volume'])

except ValueError:
    st.error("The value entered cannot be interpreted as a valid stock ticker symbol.")
import datetime
import streamlit as st
import yfinance as yf

st.write("""
            # STOCK PRICE ANALYSIS """)



symbol= st.selectbox(
    'Which Stock symbol would you like to choose for analysis?',
    ('AAPL','GOOG','TSLA','MSFT','NFLX','AMZN','NKE','JPM','FB','JNJ','DIS'))

col1,col2 = st.columns(2)

with col1:
    start_date = st.date_input("Please enter start date", datetime.date(2019,1,1))

with col2:
    end_date = st.date_input("Please enter end date", datetime.date(2022,12,31))

ticker_data =yf.Ticker(symbol)
ticker_df = ticker_data.history(period="1d", start=start_date, end=end_date)

st.write(f"""
    ### {symbol}'s Stocks """)

st.dataframe(ticker_df)

st.write(f"""
    ### {symbol}'s Closing Price Chart Analysis """)

st.line_chart(ticker_df["Close"])

st.write(f"""
    ### {symbol}'s Volumes Price Chart Analysis """)

st.line_chart(ticker_df["Volume"])

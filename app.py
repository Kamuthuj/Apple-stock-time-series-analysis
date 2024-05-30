import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import date, timedelta

# Streamlit app title
st.title("Apple Stock Price Analysis")

# Sidebar filters
st.sidebar.header('Filters')

# Date range selection
start_date = st.sidebar.date_input("Start date", date.today() - timedelta(days=365))
end_date = st.sidebar.date_input("End date", date.today())

# Fetching Apple stock data
data = yf.download('AAPL', start=start_date, end=end_date)

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=data.index,
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close'])])

fig.update_layout(title='Time Series Analysis (Candlestick Chart with Buttons and Slider)')

fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label='1m', step='month', stepmode='backward'),
            dict(count=6, label='6m', step='month', stepmode='backward'),
            dict(count=1, label='YTD', step='year', stepmode='todate'),
            dict(count=1, label='1y', step='year', stepmode='backward'),
            dict(step='all')
        ])
    )
)

fig.update_layout(width=1800, height=1000)

# Display the candlestick chart in the app
st.plotly_chart(fig, use_container_width=True)


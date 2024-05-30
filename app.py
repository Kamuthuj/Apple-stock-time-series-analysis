import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from datetime import date, timedelta

# Setting the start and end dates
d1 = date.today().strftime("%Y-%m-%d")
end_date = d1

# Calculating the date 365 days ago
d2 = date.today() - timedelta(days=365)
start_date = d2.strftime("%Y-%m-%d")

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

fig.update_layout(width=1800, height=800)

# Streamlit app
st.title("Apple Stock Price Analysis.")
st.plotly_chart(fig, use_container_width=True)

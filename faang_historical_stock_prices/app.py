import yfinance as yf
import streamlit as st

st.set_page_config(layout='wide')

st.write("""
# FAANG Simple Stock Price Visualizations

Show are the stock closing price and volume of:
1. Facebook (Meta)
2. Amazon
3. Apple
4. Netflix
5. Google
6. S&P500

""")

t_sym_fb = 'FB2A.BE'
t_sym_amz = 'AMZN'
t_sym_apl = 'AAPL'
t_sym_nfx = 'NFLX'
t_sym_ggl = 'GOOGL'
t_sym_sp500 = 'SPX'

fb_data = yf.Ticker(t_sym_fb)
am_data = yf.Ticker(t_sym_amz)
ap_data = yf.Ticker(t_sym_apl)
nf_data = yf.Ticker(t_sym_nfx)
gg_data = yf.Ticker(t_sym_ggl)
sp500_data = yf.Ticker(t_sym_sp500)

fb_df = fb_data.history(period='5d', start='2010-5-21', end='2021-12-10')
am_df = am_data.history(period='5d', start='2010-5-21', end='2021-12-10')
ap_df = ap_data.history(period='5d', start='2010-5-21', end='2021-12-10')
nf_df = nf_data.history(period='5d', start='2010-5-21', end='2021-12-10')
gg_df = gg_data.history(period='5d', start='2010-5-21', end='2021-12-10')
sp500_df = sp500_data.history(period='5d', start='2010-5-21', end='2021-12-10')

col1, col2, col3 = st.columns(3)

col1.write("""
### Facebook Closing Price
""")
col1.line_chart(fb_df.Close)

col1.write("""
### Facebook Volume Price
""")
col1.line_chart(fb_df.Volume)

col2.write("""
### Amazon Close Price
""")
col2.line_chart(am_df.Close)

col2.write("""
### Amazon Volume Price
""")
col2.line_chart(am_df.Volume)

col3.write("""
### Apple Close Price
""")
col3.line_chart(ap_df.Close)

col3.write("""
### Facebook Volume Price
""")
col3.line_chart(ap_df.Volume)

col1, col2 = st.columns(2)

col1.write("""
### Netflix Close Price
""")
col1.line_chart(nf_df.Close)

col1.write("""
### Netflix Volume Price
""")
col1.line_chart(nf_df.Volume)

col2.write("""
## Google Close Price
""")
col2.line_chart(gg_df.Close)

col2.write("""
## Google Volume Price
""")
col2.line_chart(gg_df.Volume)

st.write("""
### S&P 500 Index
Same period as FAANG companies
""")
st.write(sp500_df)
st.line_chart(sp500_df.Close)
st.line_chart(sp500_df.Volume)
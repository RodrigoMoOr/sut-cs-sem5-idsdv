import yfinance as yf
import streamlit as st
import pandas as pd


st.write("""
# FAANG Simple Stock Price Visualizations

Show are the stock closing price and volume of:
1. Facebook (Meta)
2. Amazon
3. Apple
4. Netflix
5. Google

""")

t_sym_fb = 'FB2A.BE'
t_sym_amz = 'AMZN'
t_sym_apl = 'AAPL'
t_sym_nfx = 'NFLX'
t_sym_ggl = 'GOOGL'

fb_data = yf.Ticker(t_sym_fb)
am_data = yf.Ticker(t_sym_amz)
ap_data = yf.Ticker(t_sym_apl)
nf_data = yf.Ticker(t_sym_nfx)
gg_data = yf.Ticker(t_sym_ggl)

fb_df = fb_data.history(period='5d', start='2010-5-21', end='2021-12-10')
am_df = am_data.history(period='5d', start='2010-5-21', end='2021-12-10')
ap_df = ap_data.history(period='5d', start='2010-5-21', end='2021-12-10')
nf_df = nf_data.history(period='5d', start='2010-5-21', end='2021-12-10')
gg_df = gg_data.history(period='5d', start='2010-5-21', end='2021-12-10')

st.line_chart(fb_df.Close)
st.line_chart(fb_df.Volume)

st.line_chart(am_df.Close)
st.line_chart(am_df.Volume)

st.line_chart(ap_df.Close)
st.line_chart(ap_df.Volume)

st.line_chart(nf_df.Close)
st.line_chart(nf_df.Volume)

st.line_chart(gg_df.Close)
st.line_chart(gg_df.Volume)
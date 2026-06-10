import streamlit as st
import pandas as pd

st.title("Bluestock MF Analytics Dashboard")

cagr = pd.read_csv("outputs/cagr_table.csv")

st.subheader("CAGR Analysis")
st.dataframe(cagr)

sharpe = pd.read_csv("outputs/sharpe_ratio.csv")

st.subheader("Sharpe Ratio")
st.dataframe(sharpe)    
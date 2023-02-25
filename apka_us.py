import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from openbb_terminal.sdk import openbb
import plotly.express as pxz
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ---------------------------------------------- PANDAS DATAFRAME
name = st.text_input('Type stock ticker', 'KO')

summary = openbb.stocks.fa.key(name)


st.sidebar.write('Market Cap = ' + summary.T['Market capitalization'][0])
st.sidebar.write('EPS = ' + summary.T['EPS'][0])
st.sidebar.write('PE = ' + summary.T['PE ratio'][0])
st.sidebar.write('PEG = ' + summary.T['PEG ratio'][0])


income_statement = openbb.stocks.fa.income(name)
cash_flow = openbb.stocks.fa.cash(name)

time = income_statement.columns



revenue = income_statement.T['Total revenue']
#gross_profit = income_statement.T['Gross profit']



free_cash_flow = cash_flow.T['Free cash flow']



def Revenue():
    st.subheader("Revenue")

    trace0 = go.Bar(x =time, y = revenue, name = 'Mean', marker = dict(color = 'blue'))
    data = [trace0]
    fig = go.Figure(data = data)
    st.plotly_chart(fig)



def FCF():
    st.subheader("Free Cash Flow")

    trace0 = go.Bar(x =time, y = free_cash_flow, name = 'Mean', marker = dict(color = 'green'))
    data = [trace0]
    fig = go.Figure(data = data)
    st.plotly_chart(fig)




Revenue()
FCF()

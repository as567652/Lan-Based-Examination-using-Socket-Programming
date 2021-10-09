import pandas as pd
import streamlit as st 


df = pd.read_csv("status.csv")

def highlight_survived(s):
    return ['background-color: green']*len(s) if s.started else ['background-color: red']*len(s)

def color_survived(val):
    color = 'green' if val else 'red'
    return f'background-color: {color}'

st.dataframe(df.style.apply(highlight_survived, axis=1))
st.dataframe(df.style.applymap(color_survived, subset=['started']))
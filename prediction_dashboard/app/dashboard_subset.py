
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Prediction Dashboard",
    layout="wide"
)

st.title("CST8504 Prediction Dashboard")

st.write("Welcome to our machine learning dashboard!")

# change path to change dataset
df = pd.read_csv("data/processed/Merged.csv")

st.subheader("Dataset Overview")

col1, col2 = st.columns(2)

col1.metric("Total Rows", len(df))
col2.metric("Total Columns", len(df.columns))

st.subheader("Data Preview")
st.dataframe(df.head(20))

st.subheader("Summary Statistics")
st.dataframe(df.describe(include="all"))

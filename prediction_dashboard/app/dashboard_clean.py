
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Prediction Dashboard",
    layout="wide"
)

st.title("CST8504 Prediction Dashboard")

st.write("Welcome to our machine learning dashboard!")

# change path to change dataset
df = pd.read_csv("data/processed/Clean.csv")
df_num = df.drop(columns=['Station', 'Date', 'outlier score'])
cols = df.columns.to_list()
num_cols = df_num.columns.to_list()

model_stats = pd.read_csv("data/processed/stats.csv")




st.subheader("Dataset Overview")

col1, col2 = st.columns(2)

col1.metric("Total Rows", len(df))
col2.metric("Total Columns", len(df.columns))

st.subheader("Data Preview")
st.dataframe(df.head(20))

st.subheader("Summary Statistics")
st.dataframe(df.describe(include="all"))

st.title("Charts")
c1, c2, c3 = st.columns(3)
c1.subheader("Polutant covariance")
c1x = c1.selectbox("X axis", num_cols)
c1y = c1.selectbox("Y axis", num_cols, index=1)
if c1x is not None and c1y is not None:
    c1.scatter_chart(df_num, x=c1x, y=c1y)

c2.subheader("Station over time")
c2_station = c2.selectbox("Station", df['Station'].unique().tolist())
c2_target = c2.multiselect("Polutant", num_cols)
c2.scatter_chart(df[df['Station']==c2_station], x='Date', y=c2_target)

c3.subheader("Day by Day")
c3_day = c3.selectbox("Date", df['Date'].unique().tolist())
c3_target = c3.multiselect("Polutant", num_cols, key='c3_pols')
c3.scatter_chart(df[df['Date']==c3_day], x='Station', y=c3_target)

st.title("Model Analysis")
mc1, mc2 = st.columns(2)
mc1.dataframe(model_stats)
mc2.subheader("Fine Comparison")
comp_axis = mc2.selectbox("Compare Across", ["Model Type", "Target Polutant"])
if comp_axis == "Model Type":
    polut = mc2.selectbox("Polutant", num_cols)
    mc2.dataframe(model_stats[model_stats['Polutant']==polut])
else:
    model = mc2.selectbox("Model Type", model_stats['Model'].unique().tolist())
    mc2.dataframe(model_stats[model_stats["Model"]==model])
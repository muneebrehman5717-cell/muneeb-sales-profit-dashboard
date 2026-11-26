import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Mera Dashboard", layout="wide")
st.title("Mera Pehla Dashboard")

st.write("Sir, Ye Dashboard Ban Gaya!")

data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [100, 150, 120, 200, 180, 250]
})

st.dataframe(data)

fig = px.bar(data, x="Month", y="Sales", title="Sales Chart")
st.plotly_chart(fig)

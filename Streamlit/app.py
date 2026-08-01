from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="European Banking Churn Dashboard",
    layout="wide"
)

st.title("🏦 Customer Segmentation & Churn Analytics")

# ---------------------------
# Load Dataset
# ---------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

csv_path = BASE_DIR / "Dataset" / "Processed_European_Bank.csv"

# Show path for debugging (optional)
st.write("Dataset Path:", csv_path)

# Check if file exists
if not csv_path.exists():
    st.error(f"Dataset not found!\n\nExpected location:\n{csv_path}")
    st.stop()

# Read dataset
df = pd.read_csv(csv_path)

# ---------------------------
# Sidebar Filters
# ---------------------------
st.sidebar.header("Filters")

country = st.sidebar.multiselect(
    "Select Country",
    options=df["Geography"].unique(),
    default=df["Geography"].unique()
)

gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

filtered_df = df[
    (df["Geography"].isin(country)) &
    (df["Gender"].isin(gender))
]

gender = st.sidebar.multiselect(
    "Select Gender",
    df["Gender"].unique(),
    default=df["Gender"].unique()
)

filtered_df = df[
    (df["Geography"].isin(country)) &
    (df["Gender"].isin(gender))
]

total = len(filtered_df)

churn = filtered_df["Exited"].sum()

rate = churn/total*100

avg_balance = filtered_df["Balance"].mean()

avg_salary = filtered_df["EstimatedSalary"].mean()

col1,col2,col3,col4=st.columns(4)

col1.metric("Customers",total)

col2.metric("Churn Rate",f"{rate:.2f}%")

col3.metric("Avg Balance",f"${avg_balance:,.0f}")

col4.metric("Avg Salary",f"${avg_salary:,.0f}")

country_data=filtered_df.groupby("Geography")["Exited"].mean()*100

fig=px.bar(
    country_data,
    title="Country-wise Churn Rate"
)

st.plotly_chart(fig,use_container_width=True)

gender_data=filtered_df.groupby("Gender")["Exited"].mean()*100

fig=px.bar(
    gender_data,
    title="Gender-wise Churn"
)

st.plotly_chart(fig,use_container_width=True)

age=filtered_df.groupby("Age_Group")["Exited"].mean()*100

fig=px.bar(
    age,
    title="Age Group Churn"
)

st.plotly_chart(fig,use_container_width=True)

fig=px.histogram(
    filtered_df,
    x="Balance",
    nbins=40,
    title="Balance Distribution"
)

st.plotly_chart(fig,use_container_width=True)

premium=filtered_df[
    filtered_df["Balance"]>100000
]

premium_data=premium.groupby("Geography")["Exited"].mean()*100

fig=px.bar(
    premium_data,
    title="Premium Customer Churn"
)

st.plotly_chart(fig,use_container_width=True)
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="European Banking Churn Dashboard",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Customer Segmentation & Churn Analytics")

st.markdown(
    """
    Interactive dashboard for analyzing customer churn patterns across
    geography, demographics, financial profile, tenure, and customer value.
    """
)

st.divider()


# ============================================================
# LOAD DATASET
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "Dataset" / "Processed_European_Bank.csv"


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


if not DATA_PATH.exists():
    st.error("Dataset could not be found.")
    st.write("Expected dataset location:", str(DATA_PATH))
    st.stop()


df = load_data()


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.title("🏦 Banking Analytics")
st.sidebar.header("Filters")


# Country Filter
country = st.sidebar.multiselect(
    "Select Country",
    options=df["Geography"].dropna().unique().tolist(),
    default=df["Geography"].dropna().unique().tolist(),
    key="country_filter"
)


# Gender Filter
gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].dropna().unique().tolist(),
    default=df["Gender"].dropna().unique().tolist(),
    key="gender_filter"
)


# Age Group Filter
age_group = st.sidebar.multiselect(
    "Select Age Group",
    options=df["Age_Group"].dropna().unique().tolist(),
    default=df["Age_Group"].dropna().unique().tolist(),
    key="age_filter"
)


# Credit Group Filter
credit_group = st.sidebar.multiselect(
    "Select Credit Score Group",
    options=df["Credit_Group"].dropna().unique().tolist(),
    default=df["Credit_Group"].dropna().unique().tolist(),
    key="credit_filter"
)


# Balance Group Filter
balance_group = st.sidebar.multiselect(
    "Select Balance Group",
    options=df["Balance_Group"].dropna().unique().tolist(),
    default=df["Balance_Group"].dropna().unique().tolist(),
    key="balance_filter"
)


# Tenure Group Filter
tenure_group = st.sidebar.multiselect(
    "Select Tenure Group",
    options=df["Tenure_Group"].dropna().unique().tolist(),
    default=df["Tenure_Group"].dropna().unique().tolist(),
    key="tenure_filter"
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df[
    (df["Geography"].isin(country))
    & (df["Gender"].isin(gender))
    & (df["Age_Group"].isin(age_group))
    & (df["Credit_Group"].isin(credit_group))
    & (df["Balance_Group"].isin(balance_group))
    & (df["Tenure_Group"].isin(tenure_group))
].copy()


# ============================================================
# EMPTY FILTER CHECK
# ============================================================

if filtered_df.empty:
    st.warning(
        "No customers match the selected filters. "
        "Please change the sidebar filters."
    )
    st.stop()


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_customers = len(filtered_df)

total_churned = int(filtered_df["Exited"].sum())

churn_rate = (
    total_churned / total_customers * 100
    if total_customers > 0
    else 0
)

avg_balance = filtered_df["Balance"].mean()

avg_salary = filtered_df["EstimatedSalary"].mean()

active_rate = filtered_df["IsActiveMember"].mean() * 100


premium_customers = filtered_df[
    filtered_df["Balance"] > 100000
]

if len(premium_customers) > 0:
    premium_churn_rate = premium_customers["Exited"].mean() * 100
else:
    premium_churn_rate = 0


# ============================================================
# KPI SECTION
# ============================================================

st.subheader("📊 Key Performance Indicators")

col1, col2, col3 = st.columns(3)

col1.metric(
    "👥 Total Customers",
    f"{total_customers:,}"
)

col2.metric(
    "🚪 Churned Customers",
    f"{total_churned:,}"
)

col3.metric(
    "📉 Overall Churn Rate",
    f"{churn_rate:.2f}%"
)


col4, col5, col6 = st.columns(3)

col4.metric(
    "💰 Average Balance",
    f"€{avg_balance:,.2f}"
)

col5.metric(
    "💵 Average Salary",
    f"€{avg_salary:,.2f}"
)

col6.metric(
    "🟢 Active Members",
    f"{active_rate:.2f}%"
)


st.divider()


# ============================================================
# OVERALL CHURN
# ============================================================

st.subheader("1️⃣ Overall Customer Churn")

churn_counts = (
    filtered_df["Exited"]
    .value_counts()
    .rename(index={0: "Retained", 1: "Churned"})
    .reset_index()
)

churn_counts.columns = ["Customer Status", "Customers"]


fig_churn = px.pie(
    churn_counts,
    names="Customer Status",
    values="Customers",
    hole=0.45,
    title="Overall Customer Churn Distribution"
)

st.plotly_chart(
    fig_churn,
    use_container_width=True
)


# ============================================================
# COUNTRY + GENDER
# ============================================================

st.subheader("2️⃣ Geographic & Demographic Churn")

col1, col2 = st.columns(2)


# Country Churn
country_data = (
    filtered_df
    .groupby("Geography", observed=True)["Exited"]
    .mean()
    .mul(100)
    .reset_index()
)

country_data.columns = [
    "Geography",
    "Churn Rate"
]


fig_country = px.bar(
    country_data,
    x="Geography",
    y="Churn Rate",
    text_auto=".2f",
    title="Country-wise Churn Rate (%)"
)

fig_country.update_layout(
    yaxis_title="Churn Rate (%)"
)

col1.plotly_chart(
    fig_country,
    use_container_width=True
)


# Gender Churn
gender_data = (
    filtered_df
    .groupby("Gender", observed=True)["Exited"]
    .mean()
    .mul(100)
    .reset_index()
)

gender_data.columns = [
    "Gender",
    "Churn Rate"
]


fig_gender = px.bar(
    gender_data,
    x="Gender",
    y="Churn Rate",
    text_auto=".2f",
    title="Gender-wise Churn Rate (%)"
)

fig_gender.update_layout(
    yaxis_title="Churn Rate (%)"
)

col2.plotly_chart(
    fig_gender,
    use_container_width=True
)


# ============================================================
# AGE + TENURE
# ============================================================

st.subheader("3️⃣ Age & Tenure Churn Analysis")

col1, col2 = st.columns(2)


# Age Churn
age_data = (
    filtered_df
    .groupby("Age_Group", observed=True)["Exited"]
    .mean()
    .mul(100)
    .reset_index()
)

age_data.columns = [
    "Age Group",
    "Churn Rate"
]


fig_age = px.bar(
    age_data,
    x="Age Group",
    y="Churn Rate",
    text_auto=".2f",
    title="Age Group Churn Rate (%)"
)

fig_age.update_layout(
    yaxis_title="Churn Rate (%)"
)

col1.plotly_chart(
    fig_age,
    use_container_width=True
)


# Tenure Churn
tenure_data = (
    filtered_df
    .groupby("Tenure_Group", observed=True)["Exited"]
    .mean()
    .mul(100)
    .reset_index()
)

tenure_data.columns = [
    "Tenure Group",
    "Churn Rate"
]


fig_tenure = px.bar(
    tenure_data,
    x="Tenure Group",
    y="Churn Rate",
    text_auto=".2f",
    title="Tenure Group Churn Rate (%)"
)

fig_tenure.update_layout(
    yaxis_title="Churn Rate (%)"
)

col2.plotly_chart(
    fig_tenure,
    use_container_width=True
)


# ============================================================
# CREDIT + BALANCE SEGMENT
# ============================================================

st.subheader("4️⃣ Financial Profile Analysis")

col1, col2 = st.columns(2)


# Credit Score Group
credit_data = (
    filtered_df
    .groupby("Credit_Group", observed=True)["Exited"]
    .mean()
    .mul(100)
    .reset_index()
)

credit_data.columns = [
    "Credit Group",
    "Churn Rate"
]


fig_credit = px.bar(
    credit_data,
    x="Credit Group",
    y="Churn Rate",
    text_auto=".2f",
    title="Credit Score Group Churn Rate (%)"
)

fig_credit.update_layout(
    yaxis_title="Churn Rate (%)"
)

col1.plotly_chart(
    fig_credit,
    use_container_width=True
)


# Balance Group
balance_data = (
    filtered_df
    .groupby("Balance_Group", observed=True)["Exited"]
    .mean()
    .mul(100)
    .reset_index()
)

balance_data.columns = [
    "Balance Group",
    "Churn Rate"
]


fig_balance_group = px.bar(
    balance_data,
    x="Balance Group",
    y="Churn Rate",
    text_auto=".2f",
    title="Balance Segment Churn Rate (%)"
)

fig_balance_group.update_layout(
    yaxis_title="Churn Rate (%)"
)

col2.plotly_chart(
    fig_balance_group,
    use_container_width=True
)


# ============================================================
# BALANCE DISTRIBUTION
# ============================================================

st.subheader("5️⃣ Customer Balance Distribution")

fig_balance = px.histogram(
    filtered_df,
    x="Balance",
    color="Exited",
    nbins=40,
    title="Customer Balance Distribution by Churn Status",
    labels={
        "Exited": "Churn Status",
        "Balance": "Account Balance"
    }
)

st.plotly_chart(
    fig_balance,
    use_container_width=True
)


# ============================================================
# HIGH-VALUE CUSTOMER ANALYSIS
# ============================================================

st.subheader("6️⃣ High-Value Customer Churn Explorer")

premium_col1, premium_col2, premium_col3 = st.columns(3)

premium_col1.metric(
    "💎 Premium Customers",
    f"{len(premium_customers):,}"
)

premium_col2.metric(
    "📉 Premium Churn Rate",
    f"{premium_churn_rate:.2f}%"
)

premium_lost = int(
    premium_customers["Exited"].sum()
) if len(premium_customers) > 0 else 0

premium_col3.metric(
    "⚠️ High-Value Customers Lost",
    f"{premium_lost:,}"
)


if len(premium_customers) > 0:

    premium_country = (
        premium_customers
        .groupby("Geography", observed=True)["Exited"]
        .mean()
        .mul(100)
        .reset_index()
    )

    premium_country.columns = [
        "Geography",
        "Churn Rate"
    ]

    fig_premium = px.bar(
        premium_country,
        x="Geography",
        y="Churn Rate",
        text_auto=".2f",
        title="Premium Customer Churn by Country (%)"
    )

    fig_premium.update_layout(
        yaxis_title="Churn Rate (%)"
    )

    st.plotly_chart(
        fig_premium,
        use_container_width=True
    )

else:

    st.info(
        "No premium customers are available "
        "for the selected filters."
    )


# ============================================================
# SALARY VS BALANCE
# ============================================================

st.subheader("7️⃣ Salary vs Balance Churn Pattern")

scatter_df = filtered_df.copy()

scatter_df["Churn Status"] = scatter_df[
    "Exited"
].map({
    0: "Retained",
    1: "Churned"
})


fig_scatter = px.scatter(
    scatter_df,
    x="Balance",
    y="EstimatedSalary",
    color="Churn Status",
    hover_data=[
        "Geography",
        "Gender",
        "Age",
        "CreditScore",
        "Tenure"
    ],
    title="Estimated Salary vs Account Balance"
)

fig_scatter.update_layout(
    xaxis_title="Account Balance",
    yaxis_title="Estimated Salary"
)

st.plotly_chart(
    fig_scatter,
    use_container_width=True
)


# ============================================================
# GEOGRAPHY × AGE ANALYSIS
# ============================================================

st.subheader("8️⃣ Geography × Age Churn Analysis")

geo_age = (
    filtered_df
    .groupby(
        ["Geography", "Age_Group"],
        observed=True
    )["Exited"]
    .mean()
    .mul(100)
    .reset_index()
)

geo_age.columns = [
    "Geography",
    "Age Group",
    "Churn Rate"
]


fig_geo_age = px.bar(
    geo_age,
    x="Age Group",
    y="Churn Rate",
    color="Geography",
    barmode="group",
    title="Churn Rate by Country and Age Group"
)

fig_geo_age.update_layout(
    yaxis_title="Churn Rate (%)"
)

st.plotly_chart(
    fig_geo_age,
    use_container_width=True
)


# ============================================================
# ENGAGEMENT ANALYSIS
# ============================================================

st.subheader("9️⃣ Customer Engagement & Churn")

engagement_data = (
    filtered_df
    .groupby("IsActiveMember", observed=True)["Exited"]
    .mean()
    .mul(100)
    .reset_index()
)

engagement_data["Membership Status"] = engagement_data[
    "IsActiveMember"
].map({
    0: "Inactive",
    1: "Active"
})

engagement_data.rename(
    columns={"Exited": "Churn Rate"},
    inplace=True
)


fig_engagement = px.bar(
    engagement_data,
    x="Membership Status",
    y="Churn Rate",
    text_auto=".2f",
    title="Active vs Inactive Customer Churn (%)"
)

fig_engagement.update_layout(
    yaxis_title="Churn Rate (%)"
)

st.plotly_chart(
    fig_engagement,
    use_container_width=True
)


# ============================================================
# CHURNED VS RETAINED PROFILE
# ============================================================

st.subheader("🔟 Churned vs Retained Customer Profile")

profile = (
    filtered_df
    .groupby("Exited")[
        [
            "Age",
            "CreditScore",
            "Balance",
            "EstimatedSalary",
            "Tenure",
            "NumOfProducts"
        ]
    ]
    .mean()
    .reset_index()
)

profile["Customer Status"] = profile[
    "Exited"
].map({
    0: "Retained",
    1: "Churned"
})

profile = profile[
    [
        "Customer Status",
        "Age",
        "CreditScore",
        "Balance",
        "EstimatedSalary",
        "Tenure",
        "NumOfProducts"
    ]
]

st.dataframe(
    profile.round(2),
    use_container_width=True,
    hide_index=True
)


# ============================================================
# CHURN FINANCIAL EXPOSURE
# ============================================================

st.subheader("💶 Financial Exposure from Churn")

churned_customers = filtered_df[
    filtered_df["Exited"] == 1
]

lost_balance = churned_customers[
    "Balance"
].sum()

avg_churned_balance = churned_customers[
    "Balance"
].mean()

financial_col1, financial_col2 = st.columns(2)

financial_col1.metric(
    "Total Balance Held by Churned Customers",
    f"€{lost_balance:,.2f}"
)

financial_col2.metric(
    "Average Balance of Churned Customers",
    (
        f"€{avg_churned_balance:,.2f}"
        if not pd.isna(avg_churned_balance)
        else "€0.00"
    )
)

st.caption(
    "Note: Balance held by churned customers represents financial "
    "exposure, not actual bank revenue loss."
)


# ============================================================
# DATA EXPLORER
# ============================================================

st.divider()

st.subheader("🔎 Customer Data Explorer")

st.write(
    f"Displaying **{len(filtered_df):,}** customers "
    "based on the selected filters."
)

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# DOWNLOAD FILTERED DATA
# ============================================================

csv = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    label="⬇️ Download Filtered Dataset",
    data=csv,
    file_name="filtered_european_bank_customers.csv",
    mime="text/csv"
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    ### 📌 Dashboard Purpose

    This dashboard supports segmentation-driven customer churn analysis
    across geography, demographics, customer engagement, tenure,
    credit profile and account balance.

    **Key objective:** Identify high-risk customer segments and support
    targeted customer-retention strategies.
    """
)
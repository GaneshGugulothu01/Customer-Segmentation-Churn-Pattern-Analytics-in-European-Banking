import pandas as pd
import plotly.express as px
df = pd.read_csv("Dataset/European_Bank.csv")

df.head()
df.info()

df.isnull().sum()

df.describe()
df.drop(
    ['CustomerId', 'Surname'],
    axis=1,
    inplace=True
)

print(df.info())

df['Age_Group'] = pd.cut(
    df['Age'],
    bins=[18,30,45,60,100],
    labels=['<30','30-45','46-60','60+']
)

df['Credit_Group'] = pd.cut(
    df['CreditScore'],
    bins=[0,500,700,1000],
    labels=['Low','Medium','High']
)

df['Balance_Group'] = pd.cut(
    df['Balance'],
    bins=[-1,0,50000,100000,300000],
    labels=[
        'Zero Balance',
        'Low Balance',
        'Medium Balance',
        'High Balance'
    ]
)

df['Tenure_Group'] = pd.cut(
    df['Tenure'],
    bins=[-1,2,5,10],
    labels=[
        'New',
        'Mid',
        'Long'
    ]
)

# Total customers
total_customers = len(df)

# Total churned customers
total_churned = df['Exited'].sum()

# Overall churn rate
overall_churn_rate = round(
    (total_churned / total_customers) * 100,
    2
)

# Average balance
average_balance = round(
    df['Balance'].mean(),
    2
)

# Average salary
average_salary = round(
    df['EstimatedSalary'].mean(),
    2
)

# Active member percentage
active_member_percentage = round(
    (df['IsActiveMember'].sum() / total_customers) * 100,
    2
)

# Display KPIs
print("\n------ KPI SUMMARY ------")
print("Total Customers :", total_customers)
print("Total Churned Customers :", total_churned)
print("Overall Churn Rate :", overall_churn_rate, "%")
print("Average Balance :", average_balance)
print("Average Salary :", average_salary)
print("Active Members :", active_member_percentage, "%")

# Geography-wise churn rate

country_churn = (
    df.groupby("Geography")["Exited"]
    .mean() * 100
)

print("\n------ Country-wise Churn Rate ------")
print(country_churn)

gender_churn = (
    df.groupby("Gender")["Exited"]
    .mean() * 100
)

print("\n------ Gender-wise Churn Rate ------")
print(gender_churn)

age_churn = (
    df.groupby("Age_Group")["Exited"]
    .mean() * 100
)

print("\n------ Age Group Churn Rate ------")
print(age_churn)

credit_churn = (
    df.groupby("Credit_Group")["Exited"]
    .mean() * 100
)

print("\n------ Credit Score Churn Rate ------")
print(credit_churn)

balance_churn = (
    df.groupby("Balance_Group")["Exited"]
    .mean() * 100
)

print("\n------ Balance Group Churn Rate ------")
print(balance_churn)

tenure_churn = (
    df.groupby("Tenure_Group")["Exited"]
    .mean() * 100
)

print("\n------ Tenure Group Churn Rate ------")
print(tenure_churn)

premium_customers = df[
    (df["Balance"] > 100000)
    &
    (df["EstimatedSalary"] > 100000)
]

print("\nTotal Premium Customers:")
print(len(premium_customers))

premium_churn_rate = round(
    (premium_customers["Exited"].mean()) * 100,
    2
)

print("\nPremium Customer Churn Rate:")
print(premium_churn_rate, "%")

high_value_churn = premium_customers[
    premium_customers["Exited"] == 1
]

print("\nHigh Value Customers Lost:")
print(len(high_value_churn))    

df["Risk_Score"] = 0

df.loc[df["CreditScore"] < 500, "Risk_Score"] += 2

df.loc[df["IsActiveMember"] == 0, "Risk_Score"] += 2

df.loc[df["Age"] > 50, "Risk_Score"] += 1

df.loc[df["Balance"] > 100000, "Risk_Score"] += 1

df["Risk_Level"] = pd.cut(
    df["Risk_Score"],
    bins=[-1, 2, 4, 6],
    labels=[
        "Low Risk",
        "Medium Risk",
        "High Risk"
    ]
)

print(df["Risk_Level"].value_counts())

df.to_csv(
    "Processed_European_Bank.csv",
    index=False
)

print("\nDataset Saved Successfully!")
churn_counts = df["Exited"].value_counts()

fig = px.pie(
    values=churn_counts.values,
    names=["Retained", "Churned"],
    title="Overall Customer Churn"
)
fig.write_html("Images/Overall Customer Churn.html")

fig.show()
country = (
    df.groupby("Geography")["Exited"]
    .mean()
    .reset_index()
)

country["Exited"] *= 100

fig = px.bar(
    country,
    x="Geography",
    y="Exited",
    title="Country-wise Churn Rate (%)"
)
fig.write_html("Images/Country-wise Churn Rate (%).html")
fig.show()
gender = (
    df.groupby("Gender")["Exited"]
    .mean()
    .reset_index()
)

gender["Exited"] *= 100

fig = px.bar(
    gender,
    x="Gender",
    y="Exited",
    title="Gender-wise Churn Rate (%)"
)
fig.write_html("Images/Gender-wise Churn Rate (%).html")

fig.show()
age = (
    df.groupby("Age_Group")["Exited"]
    .mean()
    .reset_index()
)

age["Exited"] *= 100

fig = px.bar(
    age,
    x="Age_Group",
    y="Exited",
    title="Age-wise Churn Rate (%)"
)
fig.write_html("Images/Age-wise Churn Rate (%)")
fig.show()
fig = px.histogram(
    df,
    x="Balance",
    title="Customer Balance Distribution"
)

fig.show()
premium_country = (
    premium_customers.groupby("Geography")["Exited"]
    .mean()
    .reset_index()
)

premium_country["Exited"] *= 100

fig = px.bar(
    premium_country,
    x="Geography",
    y="Exited",
    title="Premium Customer Churn"
)

fig.show()

fig.write_html("Images/Premium Customer Churn")
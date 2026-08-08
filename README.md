# 🏦 Customer Segmentation & Churn Pattern Analytics in European Banking

## 📊 Project Overview

Customer churn is one of the major challenges faced by retail banks. Losing existing customers can reduce customer lifetime value, increase customer acquisition costs, and create revenue instability.

This project analyzes customer churn patterns in European banking using customer demographics, financial characteristics, engagement indicators, and geographic information.

The objective is to identify high-risk customer segments, understand the factors associated with churn, analyze high-value customer losses, and provide actionable recommendations for customer retention.

---

## 🚀 Live Dashboard

### 🌐 Streamlit Dashboard

**Live Application:**  
[Open Customer Churn Analytics Dashboard](PASTE-YOUR-STREAMLIT-LINK-HERE)

The interactive dashboard allows users to:

- Explore overall customer churn
- Filter customers by country
- Filter customers by gender
- Analyze age-based churn
- Analyze balance-based churn
- Compare customer segments
- Explore premium/high-value customer churn
- View dynamic KPIs and visualizations

---

## 🎯 Business Problem

Banks often monitor overall churn rates but may not have enough visibility into the specific customer segments responsible for churn.

This project addresses the following business questions:

1. Which customer groups have the highest churn risk?
2. How does churn vary across European countries?
3. How does customer age affect churn?
4. Are female or male customers more likely to churn?
5. Does credit score influence customer churn?
6. How does account balance relate to churn?
7. Does customer tenure affect churn?
8. Are high-value customers more likely to leave?
9. What is the financial exposure associated with churn?
10. Which customer segments should banks prioritize for retention?

---

# 🎯 Project Objectives

## Primary Objectives

- Measure the overall customer churn rate.
- Identify churn patterns across customer segments.
- Compare churn behavior across France, Germany, and Spain.
- Identify high-risk customer groups.

## Secondary Objectives

- Analyze churn among high-value customers.
- Evaluate customer engagement and activity.
- Study the relationship between tenure and churn.
- Analyze demographic and financial differences between churned and retained customers.
- Develop actionable customer retention recommendations.

---

# 📁 Dataset

The project uses a European banking customer dataset containing **10,000 customer records**.

### Dataset Features

| Column | Description |
|---|---|
| CustomerId | Unique customer identifier |
| Surname | Customer surname |
| CreditScore | Customer creditworthiness |
| Geography | Customer country |
| Gender | Customer gender |
| Age | Customer age |
| Tenure | Years with the bank |
| Balance | Customer account balance |
| NumOfProducts | Number of banking products |
| HasCrCard | Credit card ownership indicator |
| IsActiveMember | Customer activity indicator |
| EstimatedSalary | Estimated annual salary |
| Exited | Customer churn indicator |

---

# 🧹 Data Preparation

The following data preparation steps were performed:

### Data Validation

- Checked dataset structure.
- Checked data types.
- Checked missing values.
- Validated binary variables.
- Verified churn labels.
- Reviewed statistical distributions.

### Data Cleaning

The following non-analytical fields were removed:

- `CustomerId`
- `Surname`

The remaining variables were used for segmentation and churn analysis.

---

# 👥 Customer Segmentation

Several derived customer segments were created.

## 🌍 Geographic Segmentation

Customers were analyzed across:

- France
- Germany
- Spain

## 🎂 Age Segmentation

Customers were grouped into:

| Age Group | Range |
|---|---|
| <30 | Under 30 |
| 30-45 | 30 to 45 |
| 46-60 | 46 to 60 |
| 60+ | Above 60 |

## 💳 Credit Score Segmentation

| Segment | Credit Score |
|---|---|
| Low | Below 500 |
| Medium | 500–700 |
| High | Above 700 |

## 💰 Balance Segmentation

Customers were grouped into:

- Zero Balance
- Low Balance
- Medium Balance
- High Balance

## ⏳ Tenure Segmentation

Customers were grouped into:

- New
- Mid-term
- Long-term

---

# 📈 Key Performance Indicators

The analysis calculates several important banking KPIs:

### Overall Churn Rate

Percentage of customers who exited the bank.

### Segment Churn Rate

Churn rate for individual customer segments.

### High-Value Customer Churn Ratio

Percentage of premium/high-value customers who churned.

### Geographic Risk

Comparison of churn exposure across countries.

### Engagement Risk

Comparison of churn between active and inactive customers.

---

# 📊 Key Results

The analysis produced the following major findings.

## Overall Customer Churn

- **Total Customers:** 10,000
- **Total Churned Customers:** 2,037
- **Overall Churn Rate:** **20.37%**

Approximately one in every five customers in the dataset has churned.

---

## 🌍 Country-wise Churn

| Country | Churn Rate |
|---|---:|
| France | 16.15% |
| Germany | **32.44%** |
| Spain | 16.67% |

### Key Insight

Germany has the highest churn rate at approximately **32.44%**, almost twice the churn level observed in France and Spain.

This indicates that Germany should receive higher priority in customer retention strategies.

---

# 👩 Gender-wise Churn

| Gender | Churn Rate |
|---|---:|
| Female | **25.07%** |
| Male | 16.46% |

### Key Insight

Female customers show a higher churn rate than male customers in this dataset.

Banks could investigate whether product suitability, customer experience, engagement, or other behavioral factors contribute to this difference.

---

# 🎂 Age-wise Churn

| Age Group | Churn Rate |
|---|---:|
| <30 | 7.50% |
| 30-45 | 15.74% |
| 46-60 | **51.12%** |
| 60+ | 24.78% |

### Key Insight

Customers aged **46–60 represent the highest-risk age group**, with a churn rate above 50%.

This segment should be investigated carefully because it represents a significant customer retention opportunity.

---

# 💳 Credit Score Churn

| Credit Segment | Churn Rate |
|---|---:|
| Low | 23.64% |
| Medium | 20.29% |
| High | 19.87% |

### Key Insight

Customers with lower credit scores show somewhat higher churn.

However, the difference is smaller than the differences observed across geography and age.

---

# 💰 Balance-wise Churn

| Balance Segment | Churn Rate |
|---|---:|
| Zero Balance | 13.82% |
| Low Balance | **34.67%** |
| Medium Balance | 19.88% |
| High Balance | 25.23% |

### Key Insight

The low-balance segment has the highest churn rate among the balance groups.

High-balance customers also show elevated churn, making them important from a financial-risk perspective.

---

# ⏳ Tenure-wise Churn

| Tenure Group | Churn Rate |
|---|---:|
| New | 21.15% |
| Mid | 20.76% |
| Long | 19.67% |

### Key Insight

Tenure has a relatively smaller impact on churn compared with age and geography.

Long-term customers have a slightly lower churn rate.

---

# 💎 High-Value Customer Analysis

Premium customers were identified using customer financial characteristics.

### Results

- **Total Premium Customers:** 2,426
- **Premium Customer Churn Rate:** 25.23%
- **High-Value Customers Lost:** 612

### Key Insight

Premium/high-value customers have a churn rate of approximately **25.23%**, which is higher than the overall churn rate of 20.37%.

This is particularly important because losing high-value customers can have a greater financial impact than losing lower-value customers.

---

# ⚠️ Risk Segmentation

Customers were also classified into risk categories.

| Risk Level | Customers |
|---|---:|
| Low Risk | 7,146 |
| Medium Risk | 2,668 |
| High Risk | 186 |

This segmentation can help banks prioritize customer retention efforts.

---

# 📊 Analytical Visualizations

The project includes interactive visualizations for:

- Overall churn distribution
- Country-wise churn
- Gender-wise churn
- Age-wise churn
- Credit score churn
- Balance segment churn
- Tenure segment churn
- Customer balance distribution
- Premium customer churn
- Customer risk distribution

---

# 🖥️ Streamlit Dashboard

The project includes an interactive Streamlit dashboard.

### Dashboard Features

- 📌 Overall churn KPI
- 👥 Customer count
- 💰 Average balance
- 💵 Average salary
- 🌍 Country filter
- 👩 Gender filter
- 📊 Interactive charts
- 💎 Premium customer analysis
- 🔎 Segment-level analysis

Users can dynamically filter the dataset and analyze how customer churn changes across different segments.

---

# 🛠️ Technologies Used

### Programming

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Plotly

### Dashboard

- Streamlit

### Development

- Jupyter Notebook
- Visual Studio Code
- Git
- GitHub

---

# 📂 Project Structure

```text
Customer-Segmentation-Churn-Pattern-Analytics-in-European-Banking/
│
├── Dataset/
│   ├── European_Bank.csv
│   └── Processed_European_Bank.csv
│
├── Images/
│   └── Project visualizations
│
├── Streamlit/
│   ├── app.py
│   └── main.py
│
├── README.md
│
└── requirements.txt

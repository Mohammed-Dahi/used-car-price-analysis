# 🚗 Used Car Price Analysis

## 📌 Project Overview

This project performs an Exploratory Data Analysis (EDA) on a used car dataset to understand the main factors associated with used car selling prices.

The analysis covers data inspection, data cleaning, feature engineering, univariate analysis, bivariate analysis, multivariate analysis, and final insights.

An interactive Streamlit dashboard was also developed to make the analysis easier to explore.

---

## 🎯 Project Objectives

- Understand the structure and quality of the dataset.
- Identify and handle missing values.
- Detect and correct invalid data.
- Remove duplicate records.
- Standardize inconsistent categorical values.
- Perform feature engineering.
- Analyze vehicle price distributions.
- Explore relationships between vehicle characteristics and selling price.
- Identify important pricing patterns.
- Build an interactive dashboard for data exploration.

---

## 📊 Dataset

The dataset contains information about used vehicles and their selling prices.

| Feature | Description |
|---|---|
| `name` | Vehicle name/model |
| `year` | Manufacturing year |
| `selling_price` | Selling price |
| `km_driven` | Kilometers driven |
| `fuel` | Fuel type |
| `seller_type` | Seller type |
| `transmission` | Transmission type |
| `owner` | Ownership history |

---

## 🧹 Data Cleaning

The original dataset contained several data quality issues, including:

- Missing values
- Duplicate records
- Invalid numerical values
- Inconsistent categorical labels
- Extreme mileage values

Missing values were handled using appropriate techniques based on the variable type.

Duplicate records were removed to improve data consistency.

Clearly invalid mileage values above 1,000,000 km were treated as data-entry errors and replaced with missing values before median imputation.

Inconsistent categorical values were standardized to improve the quality and reliability of the analysis.

---

## ⚙️ Feature Engineering

Two additional features were created during the analysis.

### Car Age

`car_age = 2026 - year`

This feature represents the approximate age of each vehicle.

### Price per Kilometer

`price_per_km = selling_price / km_driven`

This feature provides an additional perspective on vehicle pricing relative to mileage.

---

## 📈 Exploratory Data Analysis

### Univariate Analysis

The following variables were analyzed individually:

- Selling price
- Mileage
- Car age
- Fuel type
- Transmission
- Seller type
- Ownership

### Bivariate Analysis

The following relationships were explored:

- Selling price vs. car age
- Selling price vs. mileage
- Selling price vs. fuel type
- Selling price vs. transmission
- Selling price vs. ownership
- Selling price vs. seller type

### Multivariate Analysis

Multiple variables were analyzed together to identify more complex pricing patterns.

Examples include:

- Selling price vs. car age by fuel type
- Selling price vs. mileage by transmission
- Average selling price across fuel and transmission combinations

---

## 🏷️ Brand Analysis

Vehicle brands were extracted from the vehicle name.

Brands were compared based on:

- Number of vehicles
- Average selling price
- Median selling price

Only brands with a sufficient number of observations were considered for reliable comparison.

---

## 🔎 Key Insights

### 1. Vehicle Age

Newer vehicles generally have higher selling prices, while older vehicles tend to have lower resale values.

### 2. Mileage

Higher mileage generally corresponds to lower selling prices, although the relationship is not perfectly linear.

### 3. Price Distribution

Selling prices are right-skewed, with most vehicles concentrated in the lower-to-middle price range and a smaller number of premium vehicles forming a long upper tail.

### 4. Fuel Type

Petrol and diesel vehicles represent the majority of the dataset.

### 5. Transmission

Manual vehicles dominate the dataset, while automatic vehicles represent a smaller proportion.

### 6. Ownership

First-owner vehicles are the most common and generally tend to have stronger resale values than vehicles with multiple previous owners.

### 7. Seller Type

Individual sellers represent a large portion of the dataset, followed by dealers and other seller categories.

### 8. Brand

Average selling prices vary significantly across vehicle brands, indicating that brand is an important factor in used-car pricing.

### 9. Data Quality

The original dataset contained missing values, duplicates, inconsistent categorical labels, and numerical anomalies. These issues were addressed during the data cleaning and preprocessing stages.

---

## 📊 Interactive Dashboard

An interactive Streamlit dashboard was developed to provide a user-friendly way to explore the dataset.

The dashboard includes:

- Key Performance Indicators
- Selling price distribution
- Selling price vs. car age
- Selling price vs. mileage
- Average price by fuel type
- Price distribution by transmission
- Average price by ownership
- Average price by seller type
- Brand-level price analysis
- Interactive filtering

### Available Filters

- Fuel Type
- Transmission
- Seller Type
- Owner Type

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook

---
## 📁 Project Structure

```text
used-car-price-analysis/
│
├── 📂 data/
│   ├── 📂 raw/
│   │   └── 📄 car_data.csv
│   │
│   └── 📂 processed/
│       └── 📄 cleaned_car_data.csv
│
├── 📂 notebooks/
│   └── 📓 Used_Car_EDA.ipynb
│
├── 📂 dashboard/
│   └── 🐍 app.py
│
├── 📄 README.md
├── 📄 requirements.txt
└── 📄 .gitignore
```
---

## 📌 Final Dataset

After data cleaning and preprocessing, the final dataset contains:

- **3,926 records**
- **8 original columns**
- **0 missing values**
- **0 duplicate rows**

Additional engineered features were created during the analysis.

---

## 🚀 Future Improvements

Possible future improvements include:

- Building a machine learning model to predict used car prices.
- Adding advanced interactive visualizations.
- Deploying the Streamlit dashboard online.
- Adding interactive brand and model comparisons.
- Applying statistical modeling to identify the strongest price drivers.

---

## 👨‍💻 Author

**Mohammed Dahi**

Data Analysis & Data Science Project

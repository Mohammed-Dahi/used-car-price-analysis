# 🚗 Used Car Price Analysis & Prediction

## 📌 Project Overview

This project analyzes a used car dataset to understand the factors associated with used car selling prices and to build machine learning models for price prediction.

The project was developed in two stages:

- **Version 1:** Exploratory Data Analysis (EDA) and Interactive Dashboard
- **Version 2:** Regression-based Machine Learning for Car Price Prediction

The complete workflow covers data understanding, data cleaning, feature engineering, exploratory analysis, preprocessing, multicollinearity analysis, regression modeling, model evaluation, and interactive visualization.

---

## 🎯 Project Objectives

- Understand the structure and quality of the dataset.
- Identify and handle missing values.
- Detect and correct invalid data.
- Remove duplicate records.
- Standardize inconsistent categorical values.
- Perform feature engineering.
- Explore factors associated with used car prices.
- Analyze relationships between vehicle characteristics and selling price.
- Build and compare regression models.
- Evaluate model performance using multiple metrics.
- Prevent Data Leakage during preprocessing and modeling.
- Develop an interactive dashboard for data exploration.

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

The `price_per_km` feature was used for exploratory analysis but was excluded from machine learning because it is calculated using the target variable `selling_price`.

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

## 🤖 Machine Learning - Car Price Prediction

Version 2 extends the original EDA project into a supervised machine learning regression problem.

The target variable is:

`selling_price`

The goal is to predict used car selling prices based on vehicle characteristics.

### Regression Models

The following models were trained and compared:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

---

## 🔬 Multicollinearity Analysis

Multicollinearity was investigated using:

- Correlation Matrix
- Variance Inflation Factor (VIF)

A strong relationship exists between `year` and `car_age` because:

`car_age = 2026 - year`

Therefore, `year` was excluded from the final machine learning features and `car_age` was retained.

Regularization techniques such as Ridge and Lasso were also considered as possible approaches for handling multicollinearity.

---

## 📏 Feature Scaling

Standardization was applied to the numerical features used by:

- Linear Regression
- Ridge Regression
- Lasso Regression

Tree-based models were trained without feature scaling because their splitting process is generally not affected by the scale of numerical variables.

---

## 🛡️ Data Leakage Prevention

Data Leakage was carefully avoided during the machine learning workflow.

The dataset was first divided into training and testing sets.

Preprocessing was then performed using `Pipeline` and `ColumnTransformer`, ensuring that preprocessing parameters were learned from the training data only.

The `price_per_km` feature was excluded from model training because it is calculated using the target variable `selling_price`.

---

## 📊 Model Evaluation

The regression models were evaluated using:

### MAE

Mean Absolute Error measures the average absolute difference between actual and predicted prices.

Lower values indicate better performance.

### RMSE

Root Mean Squared Error gives greater weight to larger prediction errors.

Lower values indicate better performance.

### R-squared

R-squared measures the proportion of variation in selling prices explained by the model.

Higher values indicate better performance.

---

## 🔎 Regularization

Linear Regression was compared with:

- Ridge Regression
- Lasso Regression

Ridge uses L2 regularization, while Lasso uses L1 regularization.

The models were compared using RMSE and R-squared to determine whether regularization improved predictive performance.

---

## 📋 Model Comparison

All regression models were evaluated using the same train/test split and the same evaluation metrics.

The final model was selected based on its overall performance, with particular attention to RMSE, MAE, and R-squared.

The model comparison and final results are available in the machine learning notebook.

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
- Scikit-learn
- Statsmodels
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
|   └── 📓 Model.ipynb
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

- Hyperparameter tuning.
- Cross-validation.
- Advanced feature engineering.
- Building a more advanced price prediction system.
- Deploying the machine learning model.
- Connecting the prediction model directly to the Streamlit dashboard.
- Adding interactive price prediction to the dashboard.

---

## 👨‍💻 Author

**Mohammed Dahi**

Data Analysis & Data Science Project

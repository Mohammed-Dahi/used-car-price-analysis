# 🚗 Used Car Price Analysis & Machine Learning

## 📌 Project Overview

This project is an end-to-end Data Science project focused on analyzing used car data, understanding the factors associated with vehicle prices, building machine learning models for price prediction and price classification, and developing an interactive dashboard for data exploration.

The complete workflow covers data understanding, data cleaning, feature engineering, exploratory data analysis, statistical analysis, preprocessing, multicollinearity analysis, regression modeling, classification modeling, model evaluation, data leakage prevention, and interactive visualization.

---

## 🎯 Project Objectives

- Understand the structure and quality of the dataset.
- Identify and handle missing values.
- Detect and correct invalid data.
- Remove duplicate records.
- Standardize inconsistent categorical values.
- Perform meaningful feature engineering.
- Explore factors associated with used car prices.
- Analyze relationships between vehicle characteristics and selling price.
- Build and compare regression models for car price prediction.
- Build a Logistic Regression model for price classification.
- Evaluate machine learning models using appropriate performance metrics.
- Analyze multicollinearity between numerical features.
- Apply appropriate feature scaling techniques.
- Prevent data leakage throughout the machine learning workflow.
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

The original dataset contained **4,345 records and 8 columns**.

After data cleaning, the final dataset contains **3,926 records**, with **0 missing values** and **0 duplicate rows**.

---

## 🧹 Data Cleaning

The dataset contained several data quality issues, including:

- Missing values
- Duplicate records
- Invalid numerical values
- Inconsistent categorical labels
- Extreme mileage values

- **Missing Values:** Handled using appropriate techniques based on the variable type.
- **Duplicates:** Removed to improve data consistency.
- **Categorical Consistency:** Standardized to ensure consistent categories across the dataset.
- **Invalid Mileage:** Clearly invalid mileage values above **1,000,000 km** were treated as data-entry errors and replaced with missing values before median imputation.

The cleaned dataset was validated to ensure data quality before proceeding to analysis and machine learning.

---

## ⚙️ Feature Engineering

Additional features were created to provide more meaningful information about each vehicle.

### Car Age
```text
car_age = 2026 - year

```

*This feature represents the approximate age of the vehicle.*

### Price per Kilometer

```text
price_per_km = selling_price / km_driven

```

*This feature provides an additional perspective on vehicle pricing relative to mileage.*

> **Note:** The `price_per_km` feature was used during exploratory analysis but was excluded from machine learning because it is calculated using the target variable (`selling_price`), which would introduce data leakage.

A `brand` feature was also extracted from the vehicle name to support brand-level analysis and machine learning.

---

## 📈 Exploratory Data Analysis

A comprehensive Exploratory Data Analysis was performed to understand the dataset and identify important patterns.

### Univariate Analysis

The analysis included:

* Selling price distribution
* Mileage distribution
* Car age distribution
* Fuel type
* Transmission
* Seller type
* Ownership

### Bivariate Analysis

Relationships investigated included:

* Selling price vs. car age
* Selling price vs. mileage
* Selling price vs. fuel type
* Selling price vs. transmission
* Selling price vs. ownership
* Selling price vs. seller type

### Multivariate Analysis

Multiple variables were analyzed simultaneously to identify more complex pricing patterns, including:

* Selling price vs. car age by fuel type
* Selling price vs. mileage by transmission
* Average selling price across fuel and transmission combinations
* Correlation analysis between numerical variables

---

## 🏷️ Brand Analysis

Vehicle brands were extracted from the vehicle name to enable brand-level analysis. Brands were analyzed based on:

* Number of vehicles
* Average selling price
* Median selling price

*Only brands with a sufficient number of observations were considered for reliable comparison.*

---

## 🤖 Machine Learning

The project applies supervised machine learning from two complementary perspectives: numerical price prediction and binary price classification.

### Car Price Prediction

The regression task predicts the numerical `selling_price` of a used car based on its characteristics. The following regression models were trained and compared:

* Linear Regression
* Ridge Regression
* Lasso Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor

#### Regression Evaluation

The regression models were evaluated using:

* **MAE** — Mean Absolute Error
* **RMSE** — Root Mean Squared Error
* **$R^2$** — R-squared

*Lower MAE and RMSE indicate smaller prediction errors, while higher $R^2$ indicates better explanatory performance.*

---

## 🔬 Multicollinearity Analysis

Multicollinearity was investigated using:

* Correlation Matrix
* Variance Inflation Factor (VIF)

A direct relationship exists between `year` and `car_age`:

```text
car_age = 2026 - year

```

Therefore, `year` was excluded from the final machine learning feature set while `car_age` was retained. Regularization techniques such as Ridge and Lasso were also used to reduce the impact of multicollinearity.

---

## 📏 Feature Scaling

Standardization was applied to numerical features for models that benefit from scaled inputs, including:

* Linear Regression
* Ridge Regression
* Lasso Regression
* Logistic Regression

*Tree-based models were trained without feature scaling because their splitting process is generally not affected by feature magnitude.*

---

## 🛡️ Data Leakage Prevention

Data leakage was carefully prevented throughout the machine learning workflow:

* The dataset was first divided into training and testing sets before preprocessing.
* `Pipeline` and `ColumnTransformer` were used to ensure that preprocessing parameters were learned only from the training data.
* The following features were excluded when necessary:
* `selling_price` — target variable
* `price_per_km` — directly derived from the target
* `year` — redundant with `car_age`
* `name` — high-cardinality feature


* The extracted `brand` feature was retained as a more general categorical representation of the vehicle.

---

## 🧠 Price Classification

A binary classification task was developed to classify vehicles into two price categories: **Lower Price** and **Higher Price**.

The median selling price was used as the classification threshold:

```text
Median Selling Price = 350,000

```

The target variable was defined as:

* **0** $\rightarrow$ Lower Price
* **1** $\rightarrow$ Higher Price

### Class Distribution

| Class | Records | Percentage |
| --- | --- | --- |
| Lower Price | 2,143 | 54.58% |
| Higher Price | 1,783 | 45.42% |

---

## 🤖 Logistic Regression

Logistic Regression was implemented to classify vehicles into lower-price and higher-price categories. The classification workflow included:

1. Feature selection
2. Train/Test Split
3. Missing-value handling
4. Numerical feature scaling
5. Categorical feature encoding
6. Pipeline-based preprocessing
7. Logistic Regression training & prediction
8. Probability estimation

---

## 📊 Classification Model Evaluation

The Logistic Regression model was evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* ROC-AUC & ROC Curve

### Final Logistic Regression Results

| Metric | Result |
| --- | --- |
| **Accuracy** | **78.12%** |
| **ROC-AUC** | **86.45%** |

### Classification Report

| Class | Precision | Recall | F1-Score |
| --- | --- | --- | --- |
| **Lower Price** | 0.80 | 0.79 | 0.80 |
| **Higher Price** | 0.76 | 0.76 | 0.76 |

> The Logistic Regression model achieved an accuracy of **78.12%** on the unseen test dataset, with a ROC-AUC of **86.45%**.

---

## 📊 Interactive Dashboard

An interactive Streamlit dashboard was developed to provide a user-friendly interface for exploring the used car dataset.

### Dashboard Features

* Key Performance Indicators (KPIs)
* Selling price distribution
* Selling price vs. car age & mileage
* Average price by fuel type & transmission
* Average price by ownership & seller type
* Brand-level price analysis
* Interactive filtering

### Available Filters

* Fuel Type
* Transmission
* Seller Type
* Owner Type

---

## 💡 Key Insights

* Vehicle age is an important factor associated with selling price.
* Higher mileage is generally associated with lower selling prices.
* Selling prices show a right-skewed distribution with a premium-price tail.
* Petrol and Diesel vehicles represent the dominant fuel categories.
* Manual transmission represents the majority of vehicles.
* Ownership history is associated with differences in selling prices.
* Vehicle brands show differences in average and median selling prices.
* Data quality issues required careful cleaning and preprocessing.
* Vehicle characteristics can be used to classify cars into lower-price and higher-price categories.
* Logistic Regression achieved **78.12% accuracy** and **86.45% ROC-AUC** on the test dataset.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* Scikit-learn
* Statsmodels
* Streamlit
* Jupyter Notebook

---

## 📁 Project Structure

```text
used-car-price-analysis/
│
├── data/
│   ├── raw/
│   │   └── car_data.csv
│   │
│   └── processed/
│       └── cleaned_car_data.csv
│
├── notebooks/
│   ├── Used_Car_EDA.ipynb
│   └── Regression_Model.ipynb
│   └── Classifiction_Model.ipynb
│
├── dashboard/
│   └── app.py
│
├── README.md
├── requirements.txt
└── .gitignore

```

---

## 🚀 Future Improvements

* Hyperparameter tuning
* Cross-validation
* Testing additional classification algorithms
* Advanced feature engineering
* Feature selection techniques
* Comparing Logistic Regression with tree-based classification models
* Improving model performance through optimization
* Deploying the machine learning models
* Connecting the prediction models to the Streamlit dashboard
* Adding interactive price prediction and price-category prediction

---

## 👨‍💻 Author

**Mohammed Dahi**
*Data Analysis & Data Science Project*

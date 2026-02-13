# Insurance Claim Cost Prediction

## Overview
Accurate estimation of insurance claim costs is critical for pricing policies and managing financial risk.
This project predicts medical insurance charges using demographic and health-related attributes.

## Objectives
- Analyze factors affecting insurance costs
- Build regression models for cost prediction
- Interpret model results for business insights

## Dataset
Medical insurance dataset containing:
- Age
- Sex
- BMI
- Number of children
- Smoking status
- Region
- Insurance charges (target variable)

## Approach
1. Data understanding and cleaning
2. Exploratory Data Analysis (EDA)
3. Feature engineering
4. Regression modeling
5. Model interpretation

## Models Used
- Linear Regression
- Ridge & Lasso Regression
- Random Forest Regressor
- Gradient Boosting / XGBoost

## Evaluation Metrics
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

## Key Insights (To be updated)
- Smoking status significantly increases insurance cost
- Higher BMI and age correlate with higher charges
- Tree-based models outperform linear models

## Business Impact
The model can help insurance companies price policies more accurately, reduce risk,
and identify high-cost customer segments.

```
insurance-claim-cost-prediction/
├── data/
│   ├── raw/
│   │   └── insurance.csv          # Original immutable data
│   └── processed/
│       └── insurance_clean.csv    # Cleaned data ready for modeling
├── models/
│   └── insurance_model.pkl        # Trained Random Forest model (saved object)
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   ├── 04_modeling.ipynb
│   └── 05_model_interpretation.ipynb
├── reports/
│   ├── insights.md                # Business findings for stakeholders
│   └── metrics.md                 # Technical performance metrics (R2, RMSE)
├── src/
│   ├── __init__.py
│   ├── preprocessing.py           # Reusable data cleaning pipeline
│   └── train.py                   # Script to train and save the model
├── .gitignore
├── README.md                      # Project documentation
└── requirements.txt               # Python dependencies

```


## Future Improvements
- Add uncertainty estimation
- Deploy as pricing API
- Incorporate medical history features

## Model Performance
| Model | MAE | RMSE | R² Score |
|-------|-----|------|----------|
| Linear Regression | ~4181 | ~6065 | 0.78 |
| **Random Forest** | **2484** | **4576** | **0.87** 🏆 |

## Key Findings
- **Smoking is the #1 cost driver:** Smokers pay significantly higher premiums.
- **The "Obesity Multiplier":** High BMI (>30) drastically increases costs *only* for smokers.
- **Age:** Costs rise linearly with age (approx $250/year).

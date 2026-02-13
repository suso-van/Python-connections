# 📐 Model Performance Metrics

## Model Overview
* **Model Type:** Random Forest Regressor
* **Target Variable:** Insurance Charges ($)
* **Training Data:** 80% (1070 samples)
* **Testing Data:** 20% (268 samples)

## Final Results
The Random Forest model outperformed the baseline Linear Regression model by capturing non-linear interactions between BMI and Smoking.

| Metric | Linear Regression | Random Forest (Final) |
| :--- | :--- | :--- |
| **R² Score** | 0.78 | **0.87** 🏆 |
| **MAE** (Mean Absolute Error) | $4,181 | **$2,484** |
| **RMSE** (Root Mean Sq Error) | $6,065 | **$4,576** |

## Interpretation
* **R² = 0.87:** Our model explains 87% of the variance in insurance costs. This is considered excellent for this dataset.
* **MAE = $2,484:** On average, our prediction is within ~$2,500 of the actual medical cost.

## Feature Importance (Top 3)
1.  **Smoker (Yes/No):** 60% importance
2.  **BMI:** 20% importance
3.  **Age:** 13% importance
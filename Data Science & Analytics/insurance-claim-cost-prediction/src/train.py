import pandas as pd
import numpy as np
import joblib  # Standard library for saving ML models
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.pipeline import Pipeline

# Import our custom scripts
# Note: This assumes you run the script from the 'src' folder or root
try:
    from preprocessing import load_data, clean_data, split_data, get_preprocessor
except ImportError:
    # Fallback if running from root
    from src.preprocessing import load_data, clean_data, split_data, get_preprocessor

def train_and_save():
    print("🚀 Starting Training Pipeline...")

    # 1. Load & Clean Data
    # Adjust path if necessary based on where you run the script
    data_path = os.path.join('..', 'data', 'raw', 'insurance.csv')
    if not os.path.exists(data_path):
        data_path = os.path.join('data', 'raw', 'insurance.csv')
    
    print(f"   Loading data from: {data_path}")
    df = load_data(data_path)
    df = clean_data(df)

    # 2. Split Data
    X_train, X_test, y_train, y_test = split_data(df)
    print(f"   Data Split: {X_train.shape[0]} training samples")

    # 3. Create a Full Pipeline (Preprocessor + Model)
    # This bundles our data transformation and model into one object
    model_pipeline = Pipeline(steps=[
        ('preprocessor', get_preprocessor()),
        ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    # 4. Train the Model
    print("   Training Random Forest Model...")
    model_pipeline.fit(X_train, y_train)

    # 5. Evaluate
    print("   Evaluating...")
    predictions = model_pipeline.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print(f"\n🏆 Model Performance:")
    print(f"   R² Score: {r2:.4f}")
    print(f"   MAE: ${mae:.2f}")

    # 6. Save the Model
    # Create a 'models' directory if it doesn't exist
    model_dir = os.path.join('..', 'models')
    if not os.path.exists(model_dir):
        os.makedirs(model_dir, exist_ok=True)
        # Fallback for root execution
        if not os.path.exists(model_dir):
             os.makedirs('models', exist_ok=True)
             model_dir = 'models'

    model_path = os.path.join(model_dir, 'insurance_model.pkl')
    joblib.dump(model_pipeline, model_path)
    print(f"\n✅ Model saved to: {model_path}")
    print("   You can now load this file to make predictions in an app!")

if __name__ == "__main__":
    train_and_save()
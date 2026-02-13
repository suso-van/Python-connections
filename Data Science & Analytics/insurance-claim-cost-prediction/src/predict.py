import joblib
import pandas as pd
import os

def make_prediction():
    # 1. Load the trained model
    model_path = os.path.join('..', 'models', 'insurance_model.pkl')
    
    # Check if model exists
    if not os.path.exists(model_path):
        # Fallback for running from root
        model_path = os.path.join('models', 'insurance_model.pkl')
        
    print(f"Loading model from: {model_path}")
    model = joblib.load(model_path)

    # 2. Define a fake new customer
    # (30 years old, BMI 29, 1 child, Male, Smoker, Southwest)
    new_customer = pd.DataFrame({
        'age': [30],
        'bmi': [29.0],
        'children': [1],
        'sex': ['male'],
        'smoker': ['yes'],
        'region': ['southwest']
    })

    # 3. Predict Cost
    prediction = model.predict(new_customer)
    print(f"\n🔮 Predicted Insurance Cost: ${prediction[0]:,.2f}")

if __name__ == "__main__":
    make_prediction()
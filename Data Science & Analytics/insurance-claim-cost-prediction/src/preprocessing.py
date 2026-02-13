import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def load_data(filepath):
    """Loads the dataset from a CSV file."""
    return pd.read_csv(filepath)

def clean_data(df):
    """Basic cleaning: drop duplicates and handle missing values."""
    df = df.copy()
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    return df

def get_preprocessor():
    """Returns a scikit-learn ColumnTransformer for preprocessing."""
    # Define features
    numerical_features = ['age', 'bmi', 'children']
    categorical_features = ['sex', 'smoker', 'region']

    # Create transformers
    numerical_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown='ignore', drop='first')

    # Bundle preprocessing for numerical and categorical data
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    return preprocessor

def split_data(df, target_col='charges', test_size=0.2, random_state=42):
    """Splits data into train and test sets."""
    X = df.drop(target_col, axis=1)
    y = df[target_col]
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    # Test the script to make sure it works
    try:
        # Note: We use '../data/raw/insurance.csv' assuming you run this from src/ or notebooks/
        # If running from root, use 'data/raw/insurance.csv'
        df = load_data('../data/raw/insurance.csv')
        df = clean_data(df)
        X_train, X_test, y_train, y_test = split_data(df)
        print("✅ Data preprocessing script verified!")
        print(f"Training shape: {X_train.shape}")
        print(f"Testing shape: {X_test.shape}")
    except Exception as e:
        print(f"❌ Error during test: {e}")
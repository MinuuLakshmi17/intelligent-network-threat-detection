import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data():
    path = "data/raw/intrusion_data.csv"
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()

    print("Dataset shape:", df.shape)
    return df


def preprocess_data(df):
    # Remove infinity values
    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Drop missing values
    df.dropna(inplace=True)

    # Features and labels
    X = df.drop('Label', axis=1)
    y = df['Label']

    # Save feature names BEFORE scaling
    feature_names = X.columns

    # Convert labels to binary
    y = y.apply(lambda x: 0 if x == 'BENIGN' else 1)

    # Normalize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Split data ✅ (THIS WAS MISSING)
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    # Return everything
    return X_train, X_test, y_train, y_test, feature_names
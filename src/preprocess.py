import pandas as pd

def preprocess_data(path):
    df = pd.read_csv(path)
    # Cleaning and encoding
    df.dropna(inplace=True)
    df = pd.get_dummies(df, drop_first=True)
    return df

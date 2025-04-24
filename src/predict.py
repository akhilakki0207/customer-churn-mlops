import joblib
import pandas as pd

def predict(input_data):
    model = joblib.load("model/churn_model.pkl")
    df = pd.DataFrame([input_data])
    return model.predict(df)[0]

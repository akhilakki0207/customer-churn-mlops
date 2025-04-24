from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Churn prediction API"}

@app.post('/predict')
def predict(features: list):
    model = pickle.load(open('model/churn_model.pkl', 'rb'))
    prediction = model.predict([np.array(features)])
    return {"prediction": int(prediction[0])}

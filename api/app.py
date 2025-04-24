from fastapi import FastAPI
from pydantic import BaseModel
from src.predict import predict

app = FastAPI()

class CustomerData(BaseModel):
    age: int
    balance: float
    num_of_products: int
    # add more fields...

@app.post("/predict")
def predict_churn(data: CustomerData):
    result = predict(data.dict())
    return {"churn": bool(result)}

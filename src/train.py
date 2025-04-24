import joblib
from sklearn.linear_model import LogisticRegression
from src.preprocess import preprocess_data

data = preprocess_data("data/raw/churn.csv")
X = data.drop('Churn', axis=1)
y = data['Churn']

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "model/churn_model.pkl")

import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=1000, n_features=20)
clf = RandomForestClassifier()
clf.fit(X, y)
with open('model/churn_model.pkl', 'wb') as f:
    pickle.dump(clf, f)

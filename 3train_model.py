from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import pickle

# Load data
X, y = load_iris(return_X_y=True)

# Train model
clf = LogisticRegression(max_iter=200)
clf.fit(X, y)

# Save model
with open('model.pkl', 'wb') as f:
    pickle.dump(clf, f)

print("Model trained and saved as model.pkl")

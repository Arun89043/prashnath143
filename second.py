from sklearn.datasets import load_iris
import pandas as pd

# Load the dataset
data = load_iris()

# Create a DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target

# Save to CSV
df.to_csv('iris_data.csv', index=False)

print("iris_data.csv saved!")

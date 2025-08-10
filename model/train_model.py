# model/train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle
import os

# Correct relative path or use absolute path if needed
dataset_path = os.path.join(os.path.dirname(__file__), '..', 'dataset', 'Crop_recommendation.csv')

# Load dataset
df = pd.read_csv(dataset_path)

# Features and target
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Decision Tree model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Save the model
model_path = os.path.join(os.path.dirname(__file__), '..', 'decision_tree_model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as decision_tree_model.pkl")

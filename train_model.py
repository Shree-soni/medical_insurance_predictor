import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import joblib

df = pd.read_csv('insurance.csv')

# Encode categorical columns
df.replace({'sex': {'male': 0, 'female': 1}}, inplace=True)
df.replace({'smoker': {'yes': 0, 'no': 1}}, inplace=True)
df.replace({'region': {'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}}, inplace=True)

# Split data
X = df.drop(columns='charges', axis=1)
Y = df['charges']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

# Train model
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Evaluate model
train_pred = regressor.predict(X_train)
test_pred = regressor.predict(X_test)

r2_train = metrics.r2_score(Y_train, train_pred)
r2_test = metrics.r2_score(Y_test, test_pred)

print(f'R² on Train Data: {r2_train:.4f}')
print(f'R² on Test Data: {r2_test:.4f}')

# Save model
joblib.dump(regressor, 'model.pkl')
print("✅ Model saved as model.pkl")

# Test with sample input
sample = np.array([31, 1, 25.74, 0, 1, 0]).reshape(1, -1)
prediction = regressor.predict(sample)
print(f"Insurance Cost Prediction for sample input: ${prediction[0]:.2f}")
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

np.random.seed(0)
X = np.random.rand(100, 4)
y = X[:, 0] + 2 * X[:, 1] + 3 * X[:, 2] + 4 * X[:, 3] + np.random.normal(0, 0.2, 100)
data = pd.DataFrame(X, columns=['Feature1', 'Feature2', 'Feature3', 'Feature4'])
data['Target'] = y
print(data.head())

train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)
X_train = train_data[['Feature1', 'Feature2', 'Feature3', 'Feature4']]
y_train = train_data['Target']
X_test = test_data[['Feature1', 'Feature2', 'Feature3', 'Feature4']]
y_test = test_data['Target']

rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

predictions = rf.predict(X_test)

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)
print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

feature_importances = rf.feature_importances_
plt.barh(['Feature1', 'Feature2', 'Feature3', 'Feature4'], feature_importances)
plt.xlabel('Importance')
plt.title('Feature Importance')
plt.show()

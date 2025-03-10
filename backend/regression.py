import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load the data from the CSV file
data = pd.read_csv('data_updated.csv')

# Encode categorical variables
data_encoded = pd.get_dummies(data, columns=['Weather', 'Time', 'Day'])

# Define features and target variable
X = data_encoded.drop('Cost', axis=1)
y = data_encoded['Cost']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# Save the model
joblib.dump(model, 'regression_model.pkl')

# Save the model columns
model_columns = list(X.columns)
joblib.dump(model_columns, 'model_columns.pkl')

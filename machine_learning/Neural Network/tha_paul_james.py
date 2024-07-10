import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
import os

os.chdir('C:/Users/james/OneDrive/Documents/Intro to python/neural-net-tha-JamesP94/data')

# Load the dataset
financial_data = pd.read_csv('calihospital_financial.txt', delimiter='\t', header=0)

# Remove any columns with all missing values
financial_data.dropna(axis=1, how='all', inplace=True)

# Convert the 'QRT' column to datetime format for proper time series analysis
financial_data['QRT'] = financial_data['QRT'].astype(str)

financial_data['QRT'] = pd.to_datetime(financial_data['QRT'].str.replace('Q', '-'))

# Create lagged features for the 'GROP_TOT' variable
financial_data['GROP_TOT_L2'] = financial_data['GROP_TOT'].shift(2)
financial_data['GROP_TOT_L3'] = financial_data['GROP_TOT'].shift(3)
financial_data['GROP_TOT_L5'] = financial_data['GROP_TOT'].shift(5)

# Remove any rows with missing values due to shifting
financial_data.dropna(inplace=True)

# Define the features and target variable
features = financial_data[['GROP_TOT_L2', 'GROP_TOT_L3', 'GROP_TOT_L5']]
target = financial_data['GROP_TOT']

# Split the data: 70% training, 30% testing
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)

# Build and train three different ANN models
models = {
    'small': MLPRegressor(hidden_layer_sizes=(10,), random_state=1),
    'medium': MLPRegressor(hidden_layer_sizes=(50,), random_state=1),
    'large': MLPRegressor(hidden_layer_sizes=(100,), random_state=1)
}

# Train models and calculate MSE
errors = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    errors[name] = mse

# Output the MSE of each model
print("Mean Squared Errors for each model:", errors)
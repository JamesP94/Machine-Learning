import pandas as pd
import os
import numpy as np
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier


os.chdir(r'C:/Users/james/OneDrive/Documents/Intro to python/classification-ice-JamesP94/data')

# Load the datasets
reduction_data = pd.read_csv('reduction_data_new.txt', delimiter='\t')
titanic_data = pd.read_csv('titanic_data.txt', delimiter='\t')

# Select the target and predictor variables
target = 'intent01'
predictors = ['peruse01', 'peruse02', 'peruse03', 'pereou01', 'pereou02']

# Create the regression tree model
reg_tree = DecisionTreeRegressor(max_depth=5) 
reg_tree.fit(reduction_data[predictors], reduction_data[target])

# Plot the tree
plt.figure(figsize=(13,13))
plot_tree(reg_tree, filled=True, feature_names=predictors, rounded=True, proportion=False, precision=2)
plt.show()

# One-hot encode all categorical variables
categorical_vars = ['Class', 'Sex', 'Age']
x = pd.get_dummies(titanic_data[categorical_vars], drop_first=True)

# Extract the target variable
y = titanic_data['Survived']

# Fit the decision tree classifier
clf_tree = DecisionTreeClassifier(max_depth=5) 
clf_tree.fit(x, y)

# Plot the decision tree
plt.figure(figsize=(12,10))
plot_tree(clf_tree, filled=True, feature_names=x.columns, rounded=True, class_names=['Died', 'Survived'], proportion=True, precision=2)
plt.show()

# Prune the tree to 3 levels
pruned_tree = DecisionTreeClassifier(max_depth=3)
pruned_tree.fit(x, y)

# Plot the pruned tree
plt.figure(figsize=(12,10))
plot_tree(pruned_tree, filled=True, feature_names=x.columns, rounded=True, class_names=['Died', 'Survived'], proportion=True, precision=2)
plt.show()
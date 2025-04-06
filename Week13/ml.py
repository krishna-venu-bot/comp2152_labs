# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score

# Load the IRIS dataset
iris = datasets.load_iris()
print(iris)

# Extract the features and labels, as well as the feature names and label names
X = iris['data']
y = iris['target']
feature_names = iris['feature_names']
target_names = iris['target_names']

#note: you can also get access to the elements by dot (.) access operator, e.g.,
# X = iris.data

print(type(X))
print(type(y))
print(X.shape)
print(y.shape)
print(feature_names)
print(target_names)

#train a decision tree model

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# Create a decision tree classifier
clf = DecisionTreeClassifier()

# Train the model on the training data
clf.fit(X_train, y_train)

# Make predictions on the test data
y_pred = clf.predict(X_test)

print(y_test)
print(y_pred)

# use scikit-learn's accuracy_score function to calculate the accuracy
# Calculate accuracy

# use scikit-learn's accuracy_score function to calculate the accuracy
# Calculate accuracy

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy*100:.2f}%")

plt.figure(figsize=(16,10))
plot_tree(clf, filled=True, feature_names=iris.feature_names, class_names=iris.target_names, fontsize=10)
plt.show()

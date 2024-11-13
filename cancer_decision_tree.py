# import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# load the dataset
df_cancer = pd.read_csv('cancer_classification.csv')

# check for missing values in the dataset
missing_values = df_cancer.isnull().sum()

# separate features (X) and target variable (y)
# target variable is 'benign_0__mal_1', where 0 indicates benign and 1 indicates malignant
X = df_cancer.drop(columns=['benign_0__mal_1'])
y = df_cancer['benign_0__mal_1']

# split the dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# initialize and train the decision tree model
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

# make predictions on the test set
y_pred = model.predict(X_test)

# evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

# display evaluation results
print("accuracy:", accuracy)
print("confusion matrix:")
print(conf_matrix)
print("classification report:")
print(class_report)

# visualize the decision tree
plt.figure(figsize=(20, 10), dpi=1000)
plot_tree(model, filled=True, feature_names=X.columns, class_names=['Benign', 'Malignant'], rounded=True, fontsize=10)
plt.show()

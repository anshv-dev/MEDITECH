import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data =pd.read_csv("diabetes.csv")
print(data.head())

# checking null values
print(data.isnull().sum())

# checking correlation
print(data.corr())

# splitting into input and target features
X=data.drop('Outcome',axis=1)
Y=data['Outcome']

# splitting into train and test data
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)

# training the model
model=LogisticRegression()
model.fit(X_train,Y_train)

# prediction
predictions = model.predict(X_test)
print(predictions)

# Evaluation
accuracy = accuracy_score(predictions, Y_test)

print(accuracy)
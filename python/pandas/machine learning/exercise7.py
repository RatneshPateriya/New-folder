# Exercise: Build decision tree model to predict survival based on certain parameters


# CSV file is available to download at https://github.com/codebasics/py/blob/master/ML/9_decision_tree/Exercise/titanic.csv

# In this file using following columns build a model to predict if person would survive or not,
# Pclass
# Sex
# Age
# Fare
# Calculate score of your mode
import pandas as pd
df=pd.read_csv("C:\\Users\\HP\\Downloads\\titanic.csv")
print(df)
# inputs=df.drop(['PassengerId ','Name ',' SibSp','Parch',' Ticket ','Cabin','Embarked'],axis='columns',inplace=True)
# print(ints)
df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'],axis='columns',inplace=True)
# print(inputs)

# from sklearn .preprocessing import LabelEncoder
# le_Pclass=LabelEncoder()
# le_sex=LabelEncoder()
# le_Age=LabelEncoder()     

inputs=df.drop('Survived',axis='columns')
print(df)
target=df.Survived 
inputs.Sex=inputs.Sex.map({'male':1,'female':2})
print(inputs.Age[:10])
print()
# inputs.Age=inputs.Age.fillna(input.Age.mean())
# print(inputs.Age)
inputs.Age = inputs.Age.fillna(inputs.Age.mean())

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(inputs,target,train_size=0.3)
print(len(x_train))
print(len(y_train))

from sklearn import tree
model = tree.DecisionTreeClassifier()
print(model.fit(x_train,y_train))

a=model.score(x_test,y_test)
print(a)


# Predicting if a person would buy life insurnace based on his age using logistic regression
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\HP\\Downloads\\insurance_data.csv")
print(df)
print()
# plt.scatter(df['age'],df['bought_insurance'],color='red',marker='+')
# plt.show()
# print()

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(df[['age']],df.bought_insurance,train_size=0.8)
print(x_train)
print()
print(x_test)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
print(model.fit(x_train,y_train))

print()
print(x_test)
print()
y_predicted=model.predict(x_test)
print(y_predicted)
a=model.predict_proba(x_test)
print(a)

print()
b=model.score(x_test,y_test)
print(b)

print(y_predicted)
print()
print(x_test)

# model.coef_ indicates value of m in y=m*x + b equation
print(model.coef_)
print()
# model.coef_ indicates value of m in y=m*x + b equation
print(model.intercept_)
print()

import math
def sigmoid(x):
    return 1/(1+math.exp(-x))
def predicition_function(age):
    z=0.042*age-1.53
    y=sigmoid(z)
    return y
age=35
print(predicition_function(age))

age=48
print(predicition_function(age))

age=21
print(predicition_function(age))


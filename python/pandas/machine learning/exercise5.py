# Download employee retention dataset from here: https://www.kaggle.com/giripujar/hr-analytics.

# 1 Now do some exploratory data analysis to figure out which variables have direct and 
# clear impact on employee retention (i.e. whether they leave the company or continue to work)
#2 Plot bar charts showing impact of employee salaries on retention
# 3 Plot bar charts showing corelation between department and employee retention
# 4 Now build logistic regression model using variables that were narrowed down in step 1
# Measure the accuracy of the model
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\HP\\AppData\\Local\\Temp\\1131f429-9722-4f8d-b3ec-14a3ce52b2c7_archive.zip.2c7\\HR_comma_sep.csv")
print(df)
print()
retained=df[df.left==0]
print(retained.shape)
print()
left=df[df.left==1]
print(left.shape)
print()
# # print(df.groupby('left').mean())
# plt.bar(df['salary'],df.left,color='green')
# plt.show()

# plt.bar(df['Department'],df.left,color='red')
# plt.show()

subdf=df[['satisfaction_level', 'average_montly_hours','promotion_last_5years','salary']]
print(subdf)
print()
salary_dummies=pd.get_dummies(subdf.salary,prefix='salary')
df_with_dummies=pd.concat([subdf,salary_dummies],axis='columns')
print(df_with_dummies)
print()
a=df_with_dummies.drop('salary',axis='columns',inplace=True)

print(a)

x=df_with_dummies
print(x)
print()

y=df.left
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.3)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
print(model.fit(x_train,y_train))

print(model.predict(x_test))
print()
b=model.score(x_test,y_test)
print(b)
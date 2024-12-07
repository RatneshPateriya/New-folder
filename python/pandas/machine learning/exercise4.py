# Exercise
# At the same level as this notebook on github, there is an Exercise folder that
#  contains carprices.csv. This file has car sell prices for 3 different 
# models. First plot data points on a scatter plot chart to see if linear 
# regression model can be applied. If yes, then build a model that can answer following questions,

# 1) Predict price of a mercedez benz that is 4 yr old with mileage 45000

# 2) Predict price of a BMW X5 that is 7 yr old with mileage 86000

# 3) Tell me the score (accuracy) of your model. (Hint: use LinearRegression().score()

import pandas as pd
df=pd.read_csv("C:\\Users\\HP\\Downloads\\carprices.csv")
print(df)
print()

dummies=pd.get_dummies(df['Car Model'])
print(dummies.astype(int))
print()

marged=pd.concat([df,dummies.astype(int)],axis='columns')
print(marged)

print()
final=marged.drop(['Car Model','Mercedez Benz C class'],axis='columns')
print(final)

print()
s=final.drop(['Sell Price($)'],axis='columns')
print(s)

print()
t=final['Sell Price($)']
print(t)

from sklearn.linear_model import LinearRegression
dp=LinearRegression()
print(dp.fit(s,t))
print()
a=dp.score(s,t)
print(a)

b=dp.predict([[45000,4,0,0]])
print(b)
print()
c=dp.predict([[86000,7,0,1]])
print(c)



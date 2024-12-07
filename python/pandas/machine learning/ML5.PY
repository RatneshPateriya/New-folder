# import numpy as np
import pandas as pd
#import matplotlib.pyplot as mlt
df=pd.read_csv("C:\\Users\\HP\\Downloads\\homeprices (1).csv")
print(df)
print()
dummies=pd.get_dummies(df.town)
print(dummies.astype(int))
print()
marged=pd.concat([df,dummies.astype(int)],axis='columns')
print(marged) 
print()
final=marged.drop(['town'],axis='columns')
print(final)
print()
# dummy variable Trap
final =final.drop(['west windsor'],axis='columns')
print(final)
print()

x=final.drop('price',axis='columns')
print(x)

print()

y=final.price
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x,y)
a=model.predict(x)
print(a)
print()
b=model.score(x,y)
print(b)

c=model.predict([[3400,0,0]])
print(c)

print()
d=model.predict([[2800,0,1]])
print(d)


# Using sklearn OneHotEncoder
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
dfle=df
dfle.town=le.fit_transform(dfle.town)
print(dfle)
print()
x=dfle[['town','area']].values
print(x)

print()

y=dfle.price.values
print(y)

print()
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct=ColumnTransformer([('town',OneHotEncoder(),[0])],remainder='passthrough')
x=ct.fit_transform(x)
print(x)
print()

y=x[:,1:]
print(y)
print()
print(model.fit(x,y))
print()
p=model.predict([[3400,0,0]])
print(p)



# print()
# q=model.predict([[1,0,2800]])
# print(q)
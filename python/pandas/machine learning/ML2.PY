import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
df=pd.read_csv("C:\\Users\\HP\\Desktop\\New folder\\text4.csv")
print(df)
print()
a=df.bedroom.median()
print(a)
reg=linear_model.LinearRegression()
reg.fit(df[["area","bedroom","age"]],df.price)
print(reg)
print()

print(reg.coef_)

print()
d=reg.intercept_
print(d)
print()
e=reg.predict([[3500,5,35]])
print(e)

f=reg.predict([[2500,2,20]])
print(f)



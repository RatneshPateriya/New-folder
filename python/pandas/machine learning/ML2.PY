# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn import linear_model
# df=pd.read_csv("C:\\Users\\HP\\Desktop\\New folder\\text4.csv")
# print(df)
# print()
# a=df.bedroom.median()
# print(a)
# reg=linear_model.LinearRegression()
# reg.fit(df[["area","bedroom","age"]],df.price)
# print(reg)
# print()

# print(reg.coef_)

# print()
# d=reg.intercept_
# print(d)
# print()
# e=reg.predict([[3500,5,35]])
# print(e)

# f=reg.predict([[2500,2,20]])
# print(f)

# exercise2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv("C:\\Users\\HP\\Downloads\\hiring.csv")
print(df)

print()
df.experience=df.experience.fillna('zero')
print(df)
print()
from word2number import w2n
df.experience=df.experience.apply(w2n.word_to_num)
print(df)
print()
import math
medain_test_score=math.floor(df['test_score(out of 10)'].mean())
print(medain_test_score)

print()
df ["test_score(out of 10)"]=df['test_score(out of 10)'].fillna(medain_test_score)
print(df['test_score(out of 10)'])
print()

reg=linear_model.LinearRegression()
reg.fit(df[["experience","test_score(out of 10)","interview_score(out of 10)"]],df["salary($)"])
print(reg)

print()
a=reg.predict([[2,9,6]])
print(a)

print()
b=reg.predict([[12,10,10]])
print(b)


import pandas as pd 
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\HP\\Downloads\\carprices (1).csv")
print(df)
print()
# plt.scatter(df['Mileage'],df['Age(yrs)'])
# plt.show()
# print()
# plt.scatter(df['Mileage'],df['Sell Price($)'])
# plt.show()
x=df[['Mileage','Age(yrs)']]
y=df['Sell Price($)']

print(x)
print()
print(y)
print()


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
print(x_train)
print()
print(x_test)
print()
print(y_train)
print()
print(y_test)

from sklearn.linear_model import LinearRegression
clf=LinearRegression()
clf.fit(x_train,y_train)
print(x_test)

a=clf.predict(x_test)
print(a)
print()
b=clf.score(x_test,y_test)
print(b)

print()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=10)
print(x_test)
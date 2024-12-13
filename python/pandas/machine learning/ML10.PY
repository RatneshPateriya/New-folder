# Support Vector Machine Tutorial Using Python Sklearn
import pandas as pd
from sklearn.datasets import load_iris
iris=load_iris()

print(iris.feature_names)
print(iris.target_names)
df=pd.DataFrame(iris.data,columns=iris.feature_names)
print(df)
df['target']=iris.target
print(df.head())
print()
a=df[df.target==1]
print(a.head())
print()
b=df[df.target==2]
print(b.head())

print()
c=df['flower_name']=df.target.apply(lambda x:iris.target_names[x])
print(c.head())

df0=df[:50]
df1=df[50:100]
df2=df[100:]

# import matplotlib.pyplot as plt
# plt.xlabel('sepal length (cm)')
# plt.ylabel('sepal width (cm)')
# plt.scatter(df0['sepal length (cm)'],df0['sepal width (cm)'],color='blue',marker='+')
# plt.scatter(df1['sepal length (cm)'],df1['sepal width (cm)'],color='red',marker='.')
# plt.show()
# print()
# plt.xlabel('petal length (cm)')
# plt.ylabel('petal width (cm)')
# plt.scatter(df0['petal length (cm)'],df0['petal width (cm)'],color='blue',marker='+')
# plt.scatter(df1['petal length (cm)'],df1['petal width (cm)'],color='red',marker='.')
# plt.show()

from sklearn.model_selection import train_test_split

x=df.drop(['target','flower_name'],axis='columns')
y=df.target

x_tarin,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
print(len(x_tarin))

print(len(x_test))
from sklearn.svm import SVC  
model=SVC()
model.fit(x_tarin,y_train)

z=model.score(x_test,y_test)
print(z)
print()

# Tune parameters

# 1. Regularization (C)
model_c=SVC(C=10)
model_c.fit(x_tarin,y_train)
model_c.score(x_test,y_test)
print({model_c.C})
print()
model_C=SVC(gamma=10)
model_C.fit(x_tarin,y_train)
model_C.score(x_test,y_test)
print(model_C.gamma)
print()
model_linear_karnal=SVC(kernel='linear')
model_linear_karnal.fit(x_tarin,y_train)
model_linear_karnal.score(x_test,y_test)
print(model_linear_karnal)




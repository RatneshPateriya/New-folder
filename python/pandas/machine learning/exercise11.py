# Exercise for k means tutorial
# Use iris flower dataset from sklearn library and try to form clusters 
# of flowers using petal width and length features. Drop other two features for simplicity.

# Figure out if any preprocessing such as scaling would help here
# Draw elbow plot and from that figure out optimal value of k

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris=load_iris()
print(dir(iris))
df=pd.DataFrame(iris.data,columns=iris.feature_names)
print(df)
print()
df['flower']=iris.target
print(df.head())

df.drop(['sepal length (cm)','sepal width (cm)','flower'],axis='columns',inplace=True)
print(df.head(3))
print()

# preprocessing
km=KMeans(n_clusters=3)
km.fit(df)
yp=km.predict(df)

df['cluster']=yp
print(df.head(2))

df1=df[df.cluster==0]
df2=df[df.cluster==1]
df3=df[df.cluster==2]
plt.scatter(df1['petal length (cm)'],df1["petal width (cm)"],color='red')
plt.scatter(df2['petal length (cm)'],df2["petal width (cm)"],color='yellow')
plt.scatter(df3['petal length (cm)'],df3["petal width (cm)"],color='blue')
plt.show()

# Draw elbow plot and from that figure out optimal value of k
sse=[]
k_rng=range(1,10)
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(df)
    sse.append(km.inertia_)
plt.xlabel('K')
plt.ylabel('sum of squred error')
plt.plot(k_rng,sse)
plt.show()

# sse = []
# k_rng = range(1,10)
# for k in k_rng:
#     km = KMeans(n_clusters=k)
#     km.fit(df)
#     sse.append(km.inertia_)
# plt.xlabel('K')
# plt.ylabel('Sum of squared error')
# plt.plot(k_rng,sse)
# plt.show()

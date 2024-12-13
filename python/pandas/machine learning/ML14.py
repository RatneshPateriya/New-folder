from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:\\Users\\HP\\Downloads\\income.csv")
print(df)
plt.scatter(df['Age'],df['Income($)'])
plt.show()

km=KMeans(n_clusters=3)
y_predicted=km.fit_predict(df[['Age','Income($)']])
print(y_predicted)
print()
df['cluster']=y_predicted
print(df['cluster'])

# # km_cluster_centers_

df1=df[df.cluster==1]
df2=df[df.cluster==2]
df3=df[df.cluster==3]
plt.scatter(df1['Age'],df1['Income($)'],color="red")
plt.scatter(df2['Age'],df2['Income($)'],color='blue')
plt.scatter(df3['Age'],df3['Income($)'],color='green')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.show()
plt.legend()
# Preprocessing using min max scaler
scalar=MinMaxScaler()
scalar.fit(df[['Income($)']])
df['Income($)']=scalar.transform(df[['Income($)']])
scalar.fit(df[['Age']])
df['Age'] = scalar.transform(df[['Age']])

print(df.head())

plt.scatter(df['Age'],df['Income($)'])
plt.show()

df1=df[df.cluster==1]
df2=df[df.cluster==2]
df3=df[df.cluster==3]
plt.scatter(df1['Age'],df1['Income($)'],color="red")
plt.scatter(df2['Age'],df2['Income($)'],color='blue')
plt.scatter(df3['Age'],df3['Income($)'],color='green')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.show()

# Elbow Plot
see=[]
k_ran=range(0,10)
for k in k_ran:
    km=KMeans(n_clusters=k)
    km.fit(df[['Age','Income($)']])
    see.append(km.inertia_)
plt.xlabel('K')
plt.ylabel('sum of squred error')
plt.plot(k_ran,see)
plt.show()
import pandas as pd
from sklearn.datasets import load_iris

iris=load_iris()
print(iris.feature_names)
print()

print(iris.target_names)

df=pd.DataFrame(iris.data,columns=iris.feature_names)
print(df)
print()

df['target']=iris.target
print(df.head())

a=df[df.target==1].head()
print(a)
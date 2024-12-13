import pandas as pd
from sklearn.datasets import load_iris
iris=load_iris()
print(dir(iris))

df=pd.DataFrame(iris.data,columns=iris.feature_names)
print(df)

df['target']=iris.target
from sklearn.model_selection import train_test_split
x_train ,x_test,y_train,y_test=train_test_split(df.drop(['target'],axis='columns'),iris.target,test_size=0.2)
 
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
model.fit(x_train,y_train)
a=model.score(x_test,y_test)
print(a)
print()
model=RandomForestClassifier(n_estimators=40)
model.fit(x_train,y_train)
b=model.score(x_test,y_test)
print(b)

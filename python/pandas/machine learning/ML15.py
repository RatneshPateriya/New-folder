import pandas as pd
import matplotlib .pyplot as mlt

df=pd.read_csv("C:\\Users\\HP\\Downloads\\titanic (1).csv")
print(df)
df.drop(['PassengerId','Name','SibSp','Parch','Ticket','Cabin','Embarked'],axis='columns',inplace=True)
print(df.head())
print()
inputs=df.drop('Survived',axis='columns')
target=df.Survived

dummies=pd.get_dummies(inputs.Sex.astype)
print(dummies.astype(int))

inputs=pd.concat([input,dummies],axis='columns')
print(input.head(3))
print()

a=inputs.drop(['Sex','male'],axis='columns',inplace=True)
print(a)

inputs.columns[inputs.isna().any()]

print(inputs.Age[:10])

inputs.Age=inputs.Age.fillna(inputs.Age.mean())
print(inputs.Age)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(inputs,target,test_size=0.2)

from sklearn.naive_bayes import GaussianNB
model=GaussianNB()

model.fit(x_train,y_train)
b=model.score(x_test,y_test)
print(b)
print(x_test[:10])
print()
print(y_test[:10])
c=model.predict.proba(x_test[:10])
print(c)

from sklearn.model_selection import cross_val_score
d=cross_val_score(GaussianNB(),x_train,y_train,cv=5)
print(d)
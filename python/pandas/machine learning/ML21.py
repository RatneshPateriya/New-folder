# Ensemble Learning: Bagging Tutorial
# We will use pima indian diabetes dataset to predict if a person has a diabetes or 
# not based on certain features such as blood pressure, skin thickness, age etc. We will train 
# a standalone model first and then use bagging ensemble technique to check how it can improve 
# the performance of the model
import pandas as pd
df=pd.read_csv("C:\\Users\HP\\Downloads\\diabetes.csv")
print(df)
print(df.isnull().sum())
print()
print(df.describe())
print()
print(df.Outcome.value_counts())

# Train test split

x=df.drop("Outcome",axis="columns")
y=df.Outcome

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
x_scaled=scaler.fit_transform(x)
print(x_scaled[:3])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x_scaled, y, stratify=y,random_state=10)
print(x_train.shape)
print(x_test.shape)
print()

print(y_test.value_counts())

# Train using stand alone model
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
scores=cross_val_score(DecisionTreeClassifier(),x,y,cv=5)
print(scores)
print()

# Train using Bagging
from sklearn.ensemble import BaggingClassifier
bag_model=BaggingClassifier(
    base_estimator=DecisionTreeClassifier(), 
    n_estimators=100, 
    max_samples=0.8, 
    oob_score=True,
    random_state=0
)
bag_model(x_train,y_train)
print(bag_model.oob_score_)
print()
a=bag_model.score(x_test,y_test)
print(a)
  
print()
bag_model=BaggingClassifier(
    base_estimator=DecisionTreeClassifier(), 
    n_estimators=100, 
    max_samples=0.8, 
    oob_score=True,
    random_state=0
)

scores=cross_val_score(DecisionTreeClassifier,x,y,cv=5)
print(scores)

print(scores.mean())

# Train using Random Forest

from sklearn.ensemble import RandomForestClassifier
scores=cross_val_score(RandomForestClassifier(n_estimators=50),x,y,cv=5)
print(scores.mean())

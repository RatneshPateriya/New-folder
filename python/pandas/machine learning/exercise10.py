# Exercise
# Use iris flower dataset from sklearn library and use cross_val_score against 
# following models to measure the performance of each. In the end figure out the model with best performance,
# Logistic Regression
# SVM
# Decision Tree
# Random Forest
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from sklearn.datasets import load_iris
iris=load_iris()
print(dir(iris))

# df=pd.DataFrame(iris.data,columns=iris.feature_names)
# print(df)

s_score=cross_val_score(LogisticRegression(),iris.data,iris.target)
print(s_score)

print()
svm_score=cross_val_score(SVC(),iris.data,iris.target)
print(svm_score)
# Decision Tree
d_score=cross_val_score(DecisionTreeClassifier(),iris.data,iris.target)
print(d_score)

rf_score=cross_val_score(RandomForestClassifier(n_estimators=40),iris.data,iris.target)
print(rf_score)
l=np.average(rf_score)
print(l)
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from sklearn import linear_model
df=pd.read_csv("C:\\Users\\HP\\Downloads\\homeprices.csv")
print(df)
model=linear_model.LinearRegression()
model.fit(df[["area"]],df.price)
print()
print(model.coef_)

print()
a=model.intercept_
print(a)
print()

b=model.predict([[5000]])
print(b)


#save model to a file using python pickle
import pickle
with open('model_pickle','wb') as file:
    pickle.dump(model,file)

    
# Load Saved Model
with open('model_pickle','rb') as file:
   mp=pickle.load(file)
   print()
print(mp.coef_)
print()
print(mp.intercept_)
print()
d=mp.predict([[5000]])
print(d)

# Save Trained Model Using joblib
from sklearn.externals import joblib

joblib.dump(model,'model_joblib')

# Load Saved Model
mj= joblib.load('model_joblib')

print(mj.coef_)

print()

e=mj.intercept_
print(e)
f=mj.predict([[5000]])
print(f)

    


import pandas as pd 
from sklearn.datasets import load_digits
digits=load_digits()
print(dir(digits))

import matplotlib.pyplot as plt
# plt.gray()
# for i in range(4):
#     plt.matshow(digits.images[i])
#     plt.show()
df=pd.DataFrame(digits.data)
print(df)

df['target']=digits.target
print(df[0:12])

print()
# Train and the model and prediction

x=df.drop('target',axis='columns')
y=df.target

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
model.fit(x_train,y_train)
a=model.score(x_test,y_test)
print(a)

print()
y_predicted=model.predict(x_test)
# Confusion Matrix
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_predicted)
print(cm)

import matplotlib.pyplot as plt
import seaborn as sn
plt.figure(figsize=(10,7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()
import numpy as  np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
digits=load_digits()
plt.gray()
# for i in range(5):
#     plt.matshow(digits.images[i])
#     plt.show()
print(dir(digits))
print()
print(digits.data[0])
# Create and train logistic regression model

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
from sklearn.model_selection import train_test_split

x_train,x_text,y_train,y_text=train_test_split(digits.data,digits.target,test_size=0.2)

print(model.fit(x_train,y_train))

# Measure accuracy of our model
print(model.score(x_text,y_text))
print()
a=model.predict(digits.data[0:5])
print(a)
y_predicted=model.predict(x_text)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_text, y_predicted)
print(cm)

import seaborn as sn
plt.figure(figsize = (10,7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')
plt.show()
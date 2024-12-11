# Use sklearn.datasets iris flower dataset to train your model using logistic regression.
#  You need to figure out accuracy of your model and use that to predict 
# different samples in your test dataset. In iris dataset there are 150 samples containing following features,

# Sepal Length
# Sepal Width
# Petal Length
# Petal Width
# Using above 4 features you will clasify a flower in one of the three categories,

# Setosa
# Versicolour
#  Virginica


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
iris=load_iris()
plt.gray()

# for i in range(5):
#     plt.matshow(iris.images[i])
#     plt.show()
print(dir(iris))

print(iris.data[0])

from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.3)
print(model.fit(x_train,y_train))

print()
print(model.score(x_test,y_test))
print(model.predict(iris.data[0:5]))

y_predicted = model.predict(x_test)
print(y_predicted)

print()

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_predicted)
print(cm)


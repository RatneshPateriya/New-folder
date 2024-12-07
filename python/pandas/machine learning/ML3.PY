#gradient_algorithm
# import numpy as np
# import matplotlib.pyplot as plt
# def gradient_descent(x,y):
#     m_curr=b_curr=0
#     iterations=10000
#     n=len(x)
#     plt.scatter(x,y,color="red",marker='+')
#     plt.show()
#     learning_rate=0.08
#     for i in range(iterations):
#         y_predicted=m_curr*x+b_curr
#         cost=(1/n)*sum([val**2 for val in(y-y_predicted)])
#         plt.plot(x,y_predicted,color="green")
#         plt.show()
#         md=-(2/n)*sum(x*(y-y_predicted))
#         bd=-(2/n)*sum(y-y_predicted)
#         m_curr=m_curr-learning_rate * md
#         b_curr=b_curr-learning_rate * bd
#         print("m{},b{},cost{} iteration{}".format(m_curr,b_curr,cost,i))

# x=np.array([1,2,3,4,5])
# y=np.array([5,7,9,11,13])
# gradient_descent(x,y)

import numpy as np
import pandas as pd
import matplotlib .pyplot as plt
from sklearn.linear_model import LinearRegression
import math
def predict_using_sklern():
    df=pd.read_csv("C:\\Users\\HP\\Downloads\\test_scores.csv")
    r = LinearRegression()
    r.fit[df[['math']],df.cs]
    return r.coef_,r.intercept_
def gradient_descent(x,y):
    m_curr=b_curr=0
    iterations=10
    n=len(x)
    learning_rate=0.08
    for i in range(iterations):
        y_predicted=m_curr*x+b_curr
        cost=(1/n)*sum([val**2 for val in(y-y_predicted)])
        md=-(2/n)*sum(x*(y-y_predicted))
        bd=-(2/n)*sum(y-y_predicted)
        m_curr=m_curr-learning_rate * md
        b_curr=b_curr-learning_rate * bd
        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous = cost
        print("m{},b{},cost{} iteration{}".format(m_curr,b_curr,cost,i))
        return m_curr,b_curr
    if __name__=="_main_":
        df=pd.read_csv("test_score_csv")
        x=np.array(df.math)
        y=np.array(df.cs)
        m,b=gradient_descent(x,y)
        print("Using gradient descent function: Coef {} Intercept {}:".format(m,b))
        m_sklearn,b_sklearn=predict_using_sklern()
        print("using sklearn:coef{} intercept{}".format(m_sklearn,b_sklearn))







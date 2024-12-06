# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt 
# from sklearn import linear_model
# df=pd.read_csv("C:\\Users\\HP\\Desktop\\canada_per_capita_income.csv")
# print(df)

# plt.ylabel('income(US$)')
# plt.xlabel('year')
# plt.scatter(df['year'],df['income']color="red")
# plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn import linear_model

# Data load karo
df = pd.read_csv("C:\\Users\\HP\\Desktop\\canada_per_capita_income.csv")

# Scatter plot ko sahi tarike se plot karo
plt.ylabel('Income (US$)')
plt.xlabel('Year')
plt.scatter(df['year'], df['income'],color="red")
plt.show()

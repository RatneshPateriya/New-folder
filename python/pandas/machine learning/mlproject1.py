import numpy as np
import pandas as pd
import matplotlib as plt
matplotlib.rcParams("figure.figsize")=(20,10)
df=pd.read_csv("C:\\Users\\HP\Desktop\\Bengaluru_House_Data.csv")
print(df)
print(df.shape)
print(df.columns)
a=df['area_type'].unique()
print(a)
b=df['area_type'].value_counts()
print(b)
# Drop features that are not required to build our model
df1=df.drop(['society','area_type', 'balcony','availability'],axis='columns')
print(df1.shape)


# Data Cleaning: Handle NA values
print(df1.insull.sum())
print(df1.shape)

df2=df1.dropna()
print(df2.isnull.sum())
print(df2.shape)
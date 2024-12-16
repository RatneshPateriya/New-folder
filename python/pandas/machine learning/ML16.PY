import pandas as pd
df=pd.read_csv("C:\\Users\\HP\\Downloads\\spam.csv")
print(df)
a=df.groupby('category')
print(a)


import pandas as pd
from sklearn.datasets import load_digits
digits=load_digits()
digits.tatget
print(dir(digits))

print(digits.target_names)

df=pd.DataFrame(digits.data , digits.target)
print(df)
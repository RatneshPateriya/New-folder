# read functions in csv file
import pandas as pd
var =pd.read_csv("C:\\Users\\HP\\Desktop\\New folder\\text3.csv")
print(var)
print()
# var1=pd.read_csv("C:\\Users\\HP\\Desktop\\New folder\\text3.csv",nrows=3)
# print(var1)
# print()

# var2=pd.read_csv("C:\\Users\\HP\\Desktop\\New folder\\text3.csv",usecols=["income","name"])
# print(var2)

# print()
# var3=pd.read_csv("C:\\Users\\HP\\Desktop\\New folder\\text3.csv",skiprows=[2,5])
# print(var3)

# print()
# var4=pd.read_csv("C:\\Users\\HP\\Desktop\\New folder\\text3.csv",index_col="location")
# print(var4)
# print()
# var5=pd.read_csv("C:\\Users\\HP\\Desktop\\New folder\\text3.csv",header=2)
# print()

# var6=pd.read_csv("C:\\Users\\HP\\Desktop\\New folder\\text3.csv",names=["col1","col2","col3","col4"])
# print(var6)
# print()

# var7=pd.read_csv("C:\\Users\\HP\\Desktop\\New folder\\text3.csv",header=None)
# print(var7)
# print()
var8=pd.read_csv("C:\\Users\\HP\\Desktop\\New folder\\text3.csv",dtype={"income":"float"})
print(var8)

# topic->Series
# import pandas as pd
# x=[10,20,30,40,50]
# var=pd.Series(x,index=['a','b','c','d','e'],name='python')
# print(var)
# print(type(var))
# print(var[4])

# dic={"course":['c','c++','java','python'],"value":[10,20,30,40],"lavel":[4,3,2,1]}
# var=pd.Series(dic)
# print(var)
# print(var[2])
# s1=pd.Series(20,index=[1,2,3,4,5,6,7])
# print(s1)

# s2=pd.Series(20,index=[1,2,3,4,])
# print(s1+s2)


# TOPIC->DataFrame
import pandas as pd
# x=[10,20,30,40,50]
# var=pd.DataFrame(x)
# print(var)

# dic={"a":[10,20,30,40],"b":[30,20,40,50],"c":[12,23,42,54]}
# x=pd.DataFrame(dic,index=["a","b","c","d"])
# print(x)
# print(dic["b"][2])
# print(x["a"])

# list_1=([10,20,30,40],[30,40,20,10])
# var1=pd.DataFrame(list_1)
# print(var1)

# Sr={"s":pd.Series([10,20,30,40]),"r":pd.Series([10,20,30,40])}
# p=pd.DataFrame(list_1)
# print(p)



# AIRTHMETIC OPERATION
import pandas as pd
# x={"a":[10,20,30,40,50],"b":[2,4,5,6,7]}
# var=pd.DataFrame(x)
# print(var)
# var["c"]=var["a"]+var["b"]
# print(var["c"])

# var["d"]=var["a"]-var["b"]
# print(var["d"])

# var["e"]=var["a"]*var["b"]
# print(var["e"])

# var["f"]=var["a"]/var["b"]
# print(var["f"])


# var2=var["a"]<=20
# print(var2)

# var3=var["a"]>=15
# print(var3)

# INSERT AND DELETE FUNCTION

var=pd.DataFrame({"a":[10,30,40,50,20],"b":[5,6,7,8,9]})
print(var)
var.insert(1,"python",var["a"])
print(var)
var.insert(1,"python_1",[5,10,15,20,25])
print(var)
var["python_2"]=var["a"][:3]
print(var)


# delete function
var1=var.pop("b")
print(var1)

print(var)
print()

del var["a"]
print(var)

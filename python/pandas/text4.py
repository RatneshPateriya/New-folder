
# dropna and fillna function
# import pandas as pd
# var=pd.read_csv("C:\\Users\\HP\\Downloads\\people-100.csv")
# print(var)
# print()
# var.dropna(axis=1)
# print(var)
# print()
# var1=var.dropna(how="any")
# print(var1)
# var.dropna(subset=["CHANGE"])
# print(var)
# var.dropna(inplace=True)
# print(var)
# var.dropna(thresh=8)
# print(var)

# fillna


# var.fillna("python")
# print(var)

# var.fillna(method="bfill",axis=0)
# print(var)

# var.fillna(2,inplace=True)
# print(var)

# var.fillna("python",limit=2)
# print(var)


# topic->marge and concat 
# import pandas as pd
# var1=pd.DataFrame({"a":[10,20,30,40,50],"b":[1,3,5,6,7]})
# var2=pd.DataFrame({"a":[10,20,30,40,5],"c":[10,30,50,60,70]})
# # var3=pd.merge(var1,var2,on="a")
# # print(var3)
# # how=left,right,inner,outer 
# ar4=pd.merge(var1,var2,how="inner",indicator=True)
# print(var4)


# var4=pd.merge(var1,var2,left_index=True,right_index=True,suffixes=("name","is"))
# print(var4)


# concat

# import pandas as pd
# var1=pd.DataFrame({"a":[10,20,30,40,50],"b":[1,3,5,6,7]})
# var2=pd.DataFrame({"a":[10,20,30,40,5],"c":[10,30,50,60,70]})
# var3=pd.concat([var1,var2],axis=1)
# print(var3)
# print()

# var1=pd.DataFrame({"a":[10,20,30,40,50],"b":[1,3,5,6,7]})
# var2=pd.DataFrame({"a":[10,20,30],"c":[10,30,50]})
# var3=pd.concat([var1,var2],axis=1,join="outer")
# print(var3)


# var1=pd.DataFrame({"a":[10,20,30,40,50],"b":[1,3,5,6,7]})
# var2=pd.DataFrame({"a":[10,20,30,40,50],"c":[10,30,50,60,70]})
# var3=pd.concat([var1,var2],axis=0,keys=["d1","d2"])
# print(var3)



# var1=pd.DataFrame({"a":[10,20,30,40,50],"b":[1,3,5,6,7]})
# var2=pd.DataFrame({"a":[10,20,30],"c":[10,30,50]})
# var3=pd.concat([var1,var2],axis=1,join="outer")
# print(var3)

# topic->gropby
# import pandas as pd
# var=pd.DataFrame({"name":["a","b","c","d","c","a","b","a","b","c","c"],
# "S_1":[10,20,13,40,56,60,70,39,53,60,67],
# "s_2":[45,56,6,76,86,48,45,67,45,57,65]})
# var2=pd.DataFrame(var)
# print(var2)
# var_new=var.groupby("name")
# print(var_new)
# print()
# for x,y in var_new:
#     print(x)
#     print(y)
#     print()
# var2=var_new.get_group("c")
# print(var2)
# print()
# var3=var_new.min()
# print(var3)
# print() 
# var4=var_new.max()
# print(var4)
# var5=var_new.mean()
# print(var5)
# print()
# li=list(var_new)
# print(li)

# topic->join and append
# join -> join not add the same element
# var1=pd.DataFrame({"a":[10,20,30,40,50],"b":[1,3,5,6,7]})
# var2=pd.DataFrame({"d ":[1,2,3,4],"c":[10,30,49,60]})
# var3=var1.join(var2,how="outer")
# print(var3)


# var1=pd.DataFrame({"a":[10,20,30,40,50],"b":[1,3,5,6,7]},index=["a","b","c","d","e"])
# var2=pd.DataFrame({"d ":[1,2],"c":[10,30]},index=["a","b"])
# var3=var2.join(var1,how="outer",lsuffix="_12",rsuffix="_12")
# print(var3)

# append
# import pandas as pd
# var1=pd.DataFrame({"a":[10,20,30,40,50],"b":[1,3,5,6,7]})
# var2=pd.DataFrame({"c ":[1,2,3,4],"b":[10,30,49,60]})
# var3=var1.append(var2,ignore_index=True)
# print(var3)


# topic->melt and pivot function in pandas
# import pandas as pd 
# var=pd.DataFrame({"days":[1,2,3,4,5,6],"eng":[12,13,14,15,16,13],"math":[16,17,18,12,19,18]})
# var1=pd.melt(var,id_vars=["days"],var_name="python",value_name="wscube")
# print(var1)

# pivot()
# import pandas as pd
# var=pd.DataFrame({"days":[1,2,3,4,5,6],"name":["a","b","c","d","e","f"],
# "eng":[12,13,14,15,16,13],"math":[16,17,18,12,19,18]})
# # var1=var.pivot(index="days",columns="name",values="eng")
# # print(var1)

# var2=var.pivot_table(index="name",columns="eng",aggfunc="mean",margins=True)
# print(var2)

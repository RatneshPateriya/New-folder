
import pandas as pd
# dic={"a":[10,20,30,40,50],"b":[1,2,3,45,6],"c":[2,4,6,7,8]}
# d=pd.DataFrame(dic)
# print(d)
# d.to_csv("tex2.csv",index=False,header=[1,2,3])

# dic={"name":["ratnesh","rudra","om","sankalp","sumit","kavya","prince","rajit","pankej","subash","vaishnavi","ayushi",
#              "deepika","lakshay","lakhan"],"branch":["cse","ec","civil","automobile","cse","ec","civil","automobile","cse","ec","civil","automobile","ec","civil","automobile"],
#              "income":[1500000,50000,60000,70000,40000,30000,45000,60000,50000,60000,70000,40000,30000,45000,60000,],"location":
#              ["banglore","hyedrabad","pune","mumbai","grugram","banglore","hyedrabad","pune","mumbai","grugram","banglore",
#               "hyedrabad","pune","mumbai","grugram"],
              
              
#               }
# d=pd.DataFrame(dic)
# print(d)
# d.to_csv("text3.csv",index=False)

dic={"area":[2500,3000,3500,4200,6000],
    "bedroom":[2,4,5,3,7],
    "age":[20,40,35,56,23],
    "price":[400030,34000,50000,45000,35400]}
d=pd.DataFrame(dic)
print(d)
d.to_csv("text4.csv",index=False)
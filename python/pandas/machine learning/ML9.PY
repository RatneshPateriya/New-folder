# decision tree
import pandas as pd
df=pd.read_csv("C:\\Users\\HP\\Downloads\\salaries.csv")
print(df)
print()

inputs=df.drop('salary_more_then_100k',axis='columns')
target=df['salary_more_then_100k']

from sklearn.preprocessing import LabelEncoder
le_company=LabelEncoder()
le_job=LabelEncoder()
le_degree=LabelEncoder()

inputs['company_n']=le_company.fit_transform(inputs['company'])
inputs['job_n']=le_job.fit_transform(inputs['job'])
inputs['degree_n']=le_degree.fit_transform(inputs['degree'])

print(inputs)
print()

inputs_n=inputs.drop(['company','job','degree'],axis='columns')
print(inputs_n)

print(target)
print()

from sklearn import tree
model=tree.DecisionTreeClassifier()
print(model.fit(inputs_n,target))

print(model.score(inputs_n,target))

a=model.predict([[2,2,0]])
print(a)
b=model.predict([[2,0,1]])
print(b)
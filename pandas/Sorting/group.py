import pandas as pd

data = {
    "Name":['Krishna','Sachin','Rahul','Subodh','Bhupen','Sarita','Sushant'],
    "Age":[10,90,30,12,39,32,89],
    "Salary":[2000,80000,20000,30000,90000,20000,80000]
}

df = pd.DataFrame(data)

 
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)

# multiple

grouped = df.groupby(["Age","Name"])["Salary"].sum()
print('Mulitple groud')
print(grouped)
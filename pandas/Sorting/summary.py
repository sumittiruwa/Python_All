import pandas as pd

data = {
    "Name":['Krishna','Sachin','Rahul'],
    "Age":[10,90,30],
    "Salary":[2000,30000,90000]
}

df = pd.DataFrame(data)

ave_salary = df['Salary'].mean()
print(ave_salary)
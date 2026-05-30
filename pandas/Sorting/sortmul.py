# multpile sorting
import pandas as pd

data = {
    "Name":['Krishna','Sachin','Rahul'],
    "Age":[10,90,30],
    "Salary":[2000,30000,90000]
}

df = pd.DataFrame(data)

df.sort_values(by=["Age","Salary"], ascending=[True,False], inplace=True)
print("soretd by descending")
print(df)
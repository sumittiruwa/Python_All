#sorting data

#sorting data in one column sort_values()

# df.sort_values(by="column_name", True/false, inplace=True)


import pandas as pd

data = {
    "Name":['Krishna','Sachin','Rahul'],
    "Age":[10,90,30],
    "Salary":[2000,30000,90000]
}

df = pd.DataFrame(data)

df.sort_values(by="Age", ascending=False, inplace=True)
print("soretd by descending")
print(df)

import pandas as pd

data = {
    "Name":['Sumit','krihsna','subodh','sachin','bhupen', 'rahul','sarita','sushant','raxz'],
    "Age":[20,29,20,12,34,67,19,56,45],
    "Salary":[19000,20000,20000,3000,12000,90000,60000,12097,12793],
    "Performance Score":[99,23,12,34,56,78,90,98,76]
    
}

df = pd.DataFrame(data)
print(df)


# adding column while assignet

# square brackets df["column_name"] = some_Data

df["Bonus"] = df['Salary'] * 0.1
print(df)


# using insert()
# df.insert(loc, "column_name", some_data)


df.insert(0, "Emploee ID", [10,20,30,40,50,50,50,50,10])
print(df)
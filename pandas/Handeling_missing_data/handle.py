#drorna() - using this remove the missing data row or colum

import pandas as pd

data = {
    "Name":['Sumit','krihsna','subodh','sachin','bhupen', 'rahul','sarita','sushant','raxz'],
    "Age":[20,None,20,12,34,67,19,56,45],
    "Salary":[19000,20000,20000,3000,12000,90000,60000,12097,12793],
    "Performance Score":[99,23,12,34,56,78,90,98,76]
    
}

df = pd.DataFrame(data)
print(df)


df.dropna(inplace=True)
print(df)


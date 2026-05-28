"""
1- how big is your data set
2- what are the name of the columns

shape and columns 
shape - number of rows and columns
columns - attribute the name of coulmn written as an object 
"""

import pandas as pd


data = {
    "NAme":['Sumit','krihsna','subodh','sachin','bhupen', 'rahul','sarita','sushant','raxz'],
    "Age":[20,29,20,12,34,67,19,56,45],
    "Salary":[19000,20000,20000,3000,12000,90000,60000,12097,12793],
    "Performance Score":[99,23,12,34,56,78,90,98,76]
}

df = pd.DataFrame(data)
print(f'Shape:{df.shape}')
print(f'Columns Names: {df.columns}')
print(df)

 
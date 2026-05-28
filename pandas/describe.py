import pandas as pd 


#sample data 

data = {
    "NAme":['Sumit','krihsna','subodh','sachin','bhupen', 'rahul','sarita','sushant','raxz'],
    "Age":[20,29,20,12,34,67,19,56,45],
    "Salary":[19000,20000,20000,3000,12000,90000,60000,12097,12793],
    "Performance Score":[99,23,12,34,56,78,90,98,76]
}

df = pd.DataFrame(data)
print("sample Dataframe")
print(df)
print('Descripted Statistics')
print(df.describe())
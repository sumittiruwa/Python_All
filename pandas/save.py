import pandas as pd

data = {
    "Name":['Mnish','Krishna','bhupen',],
    "Age":[10,20,30],
    "city":['ktm','bhakpatpur', 'lalitpur']
    
}

df = pd.DataFrame(data)

print(df)

df.to_csv("output.csv", index=False)
 
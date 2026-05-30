import pandas as pd

data ={
    "Time":[1,2,3,4,5],
    "Value":[10,None,30,90,None]
}

df = pd.DataFrame(data)
print('Before INterpolation')
print(df)

df['Value'] = df['Value'].interpolate(method="linear")
print('Ater interpolation')
print(df)
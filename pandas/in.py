import pandas as pd

df =pd.read_json("sample_Data.json")
print('displaying the info of the data set')
print(df.info())
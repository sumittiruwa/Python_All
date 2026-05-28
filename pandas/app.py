import pandas as pd

#read data from csv file into a dataframe

df = pd.read_csv("friens.csv", encoding="latin1")
print(df)
#head() tail()
#head(n)  5 
# tail(n) datdaframe last  rows display if not n pass it will pass 5 bottom rows
import pandas as pd

#read data from csv file into a dataframe

df = pd.read_csv("friens.csv", encoding="latin1")


print('print display 2 rows of first')
print(df.head(2))

print('displa last2 rows')
print(df.tail(2))
# print(df)

# reading from execl

# df = pd.read("hello.xlxs")
# print(df)
# df.head(10)



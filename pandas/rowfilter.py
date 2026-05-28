import pandas as pd

data = {
    "Name":['Sumit','krihsna','subodh','sachin','bhupen', 'rahul','sarita','sushant','raxz'],
    "Age":[20,29,20,12,34,67,19,56,45],
    "Salary":[19000,20000,20000,3000,12000,90000,60000,12097,12793],
    "Performance Score":[99,23,12,34,56,78,90,98,76]
}

df = pd.DataFrame(data)

# single condition

high_salary = df[df['Salary'] >20000]
print('employess with salry > 20000')
print(high_salary)


#multiple condition

filtered = df[(df['Age'] > 30) & (df['Salary'] > 5000)]

print("Employees with Age > 30 and Salary > 5000")
print(filtered)


# using OR condition
filter_or = df[(df['Age'] > 35) | (df['Performance Score'] > 90)]

print("Employees older than 35 or performance score > 90")
print(filter_or)
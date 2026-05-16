age = 25
salary = 50000.0
name = "mitsu"
has_id = True
eligible = age >= 18 and has_id
if eligible:
    print(f"{name} is eligible to vote.")
else:
    print(f"{name} is not eligible to vote.")   
if not has_id:
    print(f"{name} does not have an ID.")
print(type(age)) # it will print <class 'int'>
print(type(salary)) # it will print <class 'float'>

if salary > 40000:
    print(f"{name} has a high salary.")
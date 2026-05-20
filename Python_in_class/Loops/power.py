# compute base exp uisng only multiplication in a for loop. no "or pow" allowed.

base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
result = 1
for i in range(exp):
    result = result * base
print(f"{base} raised to the power of {exp} is: {result}")
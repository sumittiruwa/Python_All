numbers = [10, 20, 10, 30, 20, 40]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("After removing duplicates:", unique)
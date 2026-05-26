# sum 1 to N

N = int(input("Enter a number: "))
total = 0   
for i in range(1, N + 1):
    total += i
    print(f"Current total after adding {i}: {total}")


# reverse a string

name = input("Enter your name: ")
reversed_name = ""
for char in name:
    reversed_name = char + reversed_name
print(f"Reversed name: {reversed_name}")
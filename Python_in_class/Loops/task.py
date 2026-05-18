# sum 1 to N

N = int(input("Enter a number: "))
total = 0   
for i in range(1, N + 1):
    total += i
    print(f"Current total after adding {i}: {total}")
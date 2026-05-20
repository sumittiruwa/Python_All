# print a right -angle triangle of tsars for a given number of rows

rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print("*" * i)  


#netsed loop

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()
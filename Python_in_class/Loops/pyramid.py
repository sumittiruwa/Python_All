# print an inverted full pyramid . stars decrease each row, centerd with spaces

rows = int(input("row:"))   

for i in range(rows, 0, -1):
    stars = 2 * i - 1 
    spaces = rows - i 
print(" " * spaces + "*" * stars)  
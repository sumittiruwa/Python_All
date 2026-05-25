n = 5

# uppper prt one
for i in range(1, n + 1):
    # spaces
    print(" " * (n - i), end="")

  
    for j in range(1, i + 1):
        print(j, end="")

  
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()

#lower prt
for i in range(n - 1, 0, -1):
    # spaces
    print(" " * (n - i), end="")

   
    for j in range(1, i + 1):
        print(j, end="")

  
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()
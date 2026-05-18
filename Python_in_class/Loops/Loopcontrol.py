# break. continue .pass

# break statement example
for i in range(1, 11):
    if i == 5:
        break
    print(i)    
# continue statement example
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
# pass statement example
for i in range(1, 11):
    if i % 2 == 0:
        pass  # Placeholder for future code
    else:
        print(i)
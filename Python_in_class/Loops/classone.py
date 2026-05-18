for i in range(1, 100):
    print(f"Hello, student {i}")



range()
for i in range(5):
    print(i, end = "")

for i in range(1, 10, 2):
    print(i, end = " ")

range(1, 10, 2)




#iterating through a list

for char in "Hello":
    print(char, end = "-")

#enumerate() function

enumrate = {"John": 25, "Alice": 30, "Bob": 22}

for idx in enumerate(enumrate, start=1):
    print(f"{idx}. {enumrate[idx]}")


# real ai/ml use
features = ["age", "height", "weight"]
for i, feat in enumerate(features, start=1):
    print(f"{i}. {feat}")


#while loop

count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1



#user name 

password = "secret"
while True:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1


password = "secret"
while True:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")
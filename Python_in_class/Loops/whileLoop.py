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


#infinite loop example

count = 0
while count < 10:
    print("wow")

#used ctlr +c to stop the infinite loop
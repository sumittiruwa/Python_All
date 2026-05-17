# . Mini Login Authentication System 
# Build a simple authentication program: 
# ● Store a predefined username and password. 
# ● Take user input. 
# ● Use logical and comparison operators to validate credentials. 
# ● Add another condition: 
# ○ If username correct but password wrong → “Incorrect Password” 
# ○ If username wrong → “User Not Found” 


username = "devil"
password = "1234"

name = input("Enter username: ")
password = input("Enter password: ")

if name == username and password == password:
    print("Login Successful")
elif name == username and password != password:
    print("Incorrect Password")
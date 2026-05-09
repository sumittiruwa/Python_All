import random
import string

# letters, numbers, and symbols
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

# combine all characters
all_characters = letters + numbers + symbols

# user input
length = int(input("Enter password length: "))

password = ""

# loop to generate password
for i in range(length):
    password += random.choice(all_characters)

print("Generated Password:", password)
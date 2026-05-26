import random

number = random.randint(1, 5)
guess = int(input("Guess number (1-5): "))

if guess == number:
    print("You Win!")
else:
    print("You Lose! Number was", number)
import random
import time

print("===================================")
print("   ROCK PAPER SCISSORS GAME")
print("===================================")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
rounds = 0

def play_round():
    global user_score, computer_score, rounds

    print("\nChoose: rock / paper / scissors")
    user = input("Your choice: ").lower()

    if user not in choices:
        print("Invalid choice!")
        return

    computer = random.choice(choices)

    print("Computer is choosing...")
    time.sleep(1)

    print("Computer chose:", computer)

    rounds += 1

    if user == computer:
        print("Result: DRAW")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("Result: YOU WIN")
        user_score += 1
    else:
        print("Result: COMPUTER WINS")
        computer_score += 1

def show_score():
    print("\n========= SCORE =========")
    print("Rounds Played:", rounds)
    print("You:", user_score)
    print("Computer:", computer_score)
    print("=========================\n")

while True:
    print("\n1. Play Round")
    print("2. Show Score")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        play_round()
    elif choice == "2":
        show_score()
    elif choice == "3":
        print("Thanks for playing!")
        break
    else:
        print("Invalid option!")
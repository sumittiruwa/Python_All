import json
import os

FILE = "accounts.json"

def load_data():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

accounts = load_data()

def create_account():
    username = input("Enter Username: ")

    if username in accounts:
        print("Account already exists!")
        return

    password = input("Enter Password: ")

    accounts[username] = {
        "password": password,
        "balance": 0,
        "history": []
    }

    save_data(accounts)
    print("Account Created Successfully!")

def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in accounts and accounts[username]["password"] == password:
        print("Login Successful!")
        user_menu(username)
    else:
        print("Invalid Credentials")

def deposit(user):
    amount = float(input("Enter Amount: "))
    accounts[user]["balance"] += amount
    accounts[user]["history"].append(f"Deposited Rs.{amount}")
    save_data(accounts)

def withdraw(user):
    amount = float(input("Enter Amount: "))

    if amount <= accounts[user]["balance"]:
        accounts[user]["balance"] -= amount
        accounts[user]["history"].append(f"Withdrawn Rs.{amount}")
        save_data(accounts)
    else:
        print("Insufficient Balance")

def transfer(user):
    receiver = input("Receiver Username: ")

    if receiver not in accounts:
        print("User Not Found")
        return

    amount = float(input("Amount: "))

    if amount <= accounts[user]["balance"]:
        accounts[user]["balance"] -= amount
        accounts[receiver]["balance"] += amount

        accounts[user]["history"].append(
            f"Transferred Rs.{amount} to {receiver}"
        )

        accounts[receiver]["history"].append(
            f"Received Rs.{amount} from {user}"
        )

        save_data(accounts)

        print("Transfer Successful")
    else:
        print("Insufficient Balance")

def history(user):
    print("\nTransaction History")
    for item in accounts[user]["history"]:
        print(item)

def user_menu(user):
    while True:
        print("\n1.Deposit")
        print("2.Withdraw")
        print("3.Transfer")
        print("4.Balance")
        print("5.History")
        print("6.Logout")

        choice = input("Enter Choice: ")

        if choice == "1":
            deposit(user)

        elif choice == "2":
            withdraw(user)

        elif choice == "3":
            transfer(user)

        elif choice == "4":
            print("Balance:", accounts[user]["balance"])

        elif choice == "5":
            history(user)

        elif choice == "6":
            break

def main():
    while True:
        print("\n=== BANK MANAGEMENT SYSTEM ===")
        print("1.Create Account")
        print("2.Login")
        print("3.Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            login()

        elif choice == "3":
            break

main()
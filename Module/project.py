import random
import math
import datetime
import os
import sys
import json


class UserSystem:
    def __init__(self):
        self.__users = []

    def add_user(self, name):
        self.__users.append(name)

    def show_users(self):
        print("Users:", self.__users)


user_system = UserSystem()


def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file)


def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except:
        return {}


data = load_data()


def guess_game():
    print("\n🎮 Guess Game Started!")
    number = random.randint(1, 5)

    guess = int(input("Guess number (1-5): "))

    if guess == number:
        print("🎉 You Win!")
    else:
        print("❌ You Lose! Number was:", number)


def student_system():
    name = input("Enter student name: ")
    marks = list(map(int, input("Enter marks: ").split()))

    total = sum(marks)
    avg = total / len(marks)

    grade = (
        "A" if avg >= 80 else
        "B" if avg >= 60 else
        "C"
    )

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "avg": avg,
        "grade": grade
    }

    data.setdefault("students", []).append(student)
    save_data(data)

    print("Student saved!")


def show_time():
    print("Current Time:", datetime.datetime.now())


def show_files():
    print(os.listdir())


def system_info():
    print("Python Version:", sys.version)


def math_tool():
    num = int(input("Enter number: "))

    print("Square Root:", math.sqrt(num))
    print("Square:", math.pow(num, 2))
    print("Factorial:", math.factorial(num))


def show_students():
    students = data.get("students", [])
    for s in students:
        print(s)


def menu():
    while True:
        print("\n===== SMART SYSTEM =====")
        print("1. Guess Game")
        print("2. Add Student")
        print("3. Show Students")
        print("4. Show Time")
        print("5. Show Files")
        print("6. System Info")
        print("7. Math Tool")
        print("8. Add User")
        print("9. Show Users")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            guess_game()

        elif choice == "2":
            student_system()

        elif choice == "3":
            show_students()

        elif choice == "4":
            show_time()

        elif choice == "5":
            show_files()

        elif choice == "6":
            system_info()

        elif choice == "7":
            math_tool()

        elif choice == "8":
            name = input("Enter user name: ")
            user_system.add_user(name)

        elif choice == "9":
            user_system.show_users()

        elif choice == "10":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


menu()
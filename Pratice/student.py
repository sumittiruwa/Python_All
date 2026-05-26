import json
import os

FILE_NAME = "students.json"


def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# ----------------- Core Functions -----------------

def add_student():
    print("\n--- Add Student ---")
    name = input("Enter name: ")
    age = input("Enter age: ")
    roll = input("Enter roll number: ")

    students = load_data()

    # check duplicate roll
    for s in students:
        if s["roll"] == roll:
            print(" Roll number already exists!")
            return

    student = {
        "name": name,
        "age": age,
        "roll": roll
    }

    students.append(student)
    save_data(students)

    print(" Student added successfully!")

def view_students():
    print("\n--- All Students ---")
    students = load_data()

    if not students:
        print("No students found.")
        return

    for i, s in enumerate(students, start=1):
        print(f"{i}. Name: {s['name']} | Age: {s['age']} | Roll: {s['roll']}")

def search_student():
    print("\n--- Search Student ---")
    roll = input("Enter roll number: ")

    students = load_data()

    for s in students:
        if s["roll"] == roll:
            print(f"Found: Name={s['name']}, Age={s['age']}, Roll={s['roll']}")
            return

    print(" Student not found!")

def update_student():
    print("\n--- Update Student ---")
    roll = input("Enter roll number to update: ")

    students = load_data()

    for s in students:
        if s["roll"] == roll:
            print("Leave blank if you don't want to change")

            new_name = input(f"New name ({s['name']}): ")
            new_age = input(f"New age ({s['age']}): ")

            if new_name:
                s["name"] = new_name
            if new_age:
                s["age"] = new_age

            save_data(students)
            print("Student updated successfully!")
            return

    print(" Student not found!")

def delete_student():
    print("\n--- Delete Student ---")
    roll = input("Enter roll number to delete: ")

    students = load_data()

    new_students = [s for s in students if s["roll"] != roll]

    if len(new_students) == len(students):
        print(" Student not found!")
        return

    save_data(new_students)
    print(" Student deleted successfully!")

# ----------------- Main Menu -----------------

def menu():
    while True:
        print("\n==============================")
        print(" STUDENT MANAGEMENT SYSTEM ")
        print("==============================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice!")


menu()
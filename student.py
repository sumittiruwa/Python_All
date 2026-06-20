import json
import os
from datetime import datetime

FILE_NAME = "students.json"

# -----------------------------
# Colors
# -----------------------------
class Color:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

# -----------------------------
# Load Database
# -----------------------------
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# -----------------------------
# Save Database
# -----------------------------
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

students = load_data()

# -----------------------------
# Login
# -----------------------------
def login():
    print(Color.BLUE + "\n========= LOGIN =========" + Color.END)

    username = input("Username : ")
    password = input("Password : ")

    if username == "admin" and password == "admin123":
        print(Color.GREEN + "\nLogin Successful!\n" + Color.END)
    else:
        print(Color.RED + "\nInvalid Username or Password\n" + Color.END)
        exit()

# -----------------------------
# Generate Grade
# -----------------------------
def grade(mark):

    if mark >= 90:
        return "A+"

    elif mark >= 80:
        return "A"

    elif mark >= 70:
        return "B"

    elif mark >= 60:
        return "C"

    elif mark >= 50:
        return "D"

    else:
        return "F"

# -----------------------------
# Add Student
# -----------------------------
def add_student():

    print("\n------ Add Student ------")

    sid = input("Student ID : ")

    for s in students:
        if s["id"] == sid:
            print("Student ID already exists.")
            return

    name = input("Name : ")
    age = input("Age : ")
    course = input("Course : ")

    marks = float(input("Marks : "))

    student = {

        "id": sid,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks,
        "grade": grade(marks),
        "created": datetime.now().strftime("%d-%m-%Y %H:%M")

    }

    students.append(student)

    save_data(students)

    print(Color.GREEN + "\nStudent Added Successfully.\n" + Color.END)

# -----------------------------
# View Students
# -----------------------------
def view_students():

    if len(students) == 0:
        print("\nNo Records Found.\n")
        return

    print("\n================ STUDENTS ================\n")

    print("{:<8}{:<20}{:<8}{:<15}{:<10}{:<8}".format(
        "ID","Name","Age","Course","Marks","Grade"))

    print("-"*70)

    for s in students:

        print("{:<8}{:<20}{:<8}{:<15}{:<10}{:<8}".format(
            s["id"],
            s["name"],
            s["age"],
            s["course"],
            s["marks"],
            s["grade"]
        ))

# -----------------------------
# Search
# -----------------------------
def search_student():

    sid = input("\nEnter Student ID : ")

    for s in students:

        if s["id"] == sid:

            print("\nStudent Found\n")

            for key,value in s.items():
                print(key.capitalize(),":",value)

            return

    print("Student Not Found.")

# -----------------------------
# Delete
# -----------------------------
def delete_student():

    sid = input("\nEnter Student ID : ")

    for s in students:

        if s["id"] == sid:

            students.remove(s)

            save_data(students)

            print("Deleted Successfully.")

            return

    print("Student Not Found.")

# -----------------------------
# Update
# -----------------------------
def update_student():

    sid = input("\nStudent ID : ")

    for s in students:

        if s["id"] == sid:

            print("\nLeave Blank to Keep Old Value\n")

            name = input("New Name : ")

            age = input("New Age : ")

            course = input("New Course : ")

            marks = input("New Marks : ")

            if name:
                s["name"] = name

            if age:
                s["age"] = age

            if course:
                s["course"] = course

            if marks:

                marks = float(marks)

                s["marks"] = marks

                s["grade"] = grade(marks)

            save_data(students)

            print("\nUpdated Successfully.\n")

            return

    print("Student Not Found.")

# -----------------------------
# Statistics
# -----------------------------
def statistics():

    if len(students)==0:
        print("\nNo Records.\n")
        return

    total=0

    highest=students[0]["marks"]

    lowest=students[0]["marks"]

    topper=""

    for s in students:

        total+=s["marks"]

        if s["marks"]>highest:

            highest=s["marks"]

            topper=s["name"]

        if s["marks"]<lowest:

            lowest=s["marks"]

    average=total/len(students)

    print("\n========== REPORT ==========")

    print("Total Students :",len(students))

    print("Average Marks :",round(average,2))

    print("Highest Marks :",highest)

    print("Lowest Marks :",lowest)

    if topper!="":
        print("Topper :",topper)

# -----------------------------
# Menu
# -----------------------------
def menu():

    while True:

        print(Color.HEADER)

        print("""
====================================
      STUDENT MANAGEMENT SYSTEM
====================================

1. Add Student

2. View Students

3. Search Student

4. Update Student

5. Delete Student

6. Statistics

7. Exit

====================================
""")

        print(Color.END)

        choice=input("Choose Option : ")

        if choice=="1":

            add_student()

        elif choice=="2":

            view_students()

        elif choice=="3":

            search_student()

        elif choice=="4":

            update_student()

        elif choice=="5":

            delete_student()

        elif choice=="6":

            statistics()

        elif choice=="7":

            print("\nThank You.\n")
            break

        else:
            print("Invalid Choice")

# -----------------------------
# Main
# -----------------------------
if __name__=="__main__":

    login()

    menu()
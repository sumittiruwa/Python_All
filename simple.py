from dataclasses import dataclass, asdict
from pathlib import Path
import json


FILE = Path("students.json")


@dataclass
class Student:
    id: int
    name: str
    age: int
    course: str
    marks: float

    @property
    def grade(self):
        if self.marks >= 80:
            return "A+"
        elif self.marks >= 70:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "F"


class StudentManager:

    def __init__(self):
        self.students: list[Student] = []
        self.load_data()

    def load_data(self):
        if FILE.exists():
            try:
                data = json.loads(FILE.read_text())
                self.students = [Student(**student) for student in data]
            except (json.JSONDecodeError, TypeError):
                print("Could not load student data.")

    def save_data(self):
        data = [asdict(student) for student in self.students]
        FILE.write_text(json.dumps(data, indent=4))

    def add_student(self):
        try:
            student_id = int(input("Enter ID: "))

            if any(s.id == student_id for s in self.students):
                print("ID already exists!")
                return

            name = input("Enter name: ")
            age = int(input("Enter age: "))
            course = input("Enter course: ")
            marks = float(input("Enter marks: "))

            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                return

            student = Student(
                student_id,
                name,
                age,
                course,
                marks
            )

            self.students.append(student)
            self.save_data()

            print("Student added successfully!")

        except ValueError:
            print("Invalid input!")

    def show_students(self):
        if not self.students:
            print("No students found.")
            return

        print("\n--- Student List ---")

        for student in self.students:
            print(
                f"ID: {student.id} | "
                f"Name: {student.name} | "
                f"Course: {student.course} | "
                f"Marks: {student.marks} | "
                f"Grade: {student.grade}"
            )

    def search_student(self):
        keyword = input("Enter student name: ").lower()

        results = [
            student for student in self.students
            if keyword in student.name.lower()
        ]

        if not results:
            print("Student not found.")
            return

        for student in results:
            print(
                f"{student.id} - {student.name} - "
                f"{student.course} - {student.grade}"
            )

    def delete_student(self):
        try:
            student_id = int(input("Enter student ID: "))

            for student in self.students:
                if student.id == student_id:
                    self.students.remove(student)
                    self.save_data()
                    print("Student deleted!")
                    return

            print("Student not found.")

        except ValueError:
            print("Invalid ID.")

    def statistics(self):
        if not self.students:
            print("No data available.")
            return

        total = len(self.students)
        average = sum(s.marks for s in self.students) / total
        highest = max(self.students, key=lambda s: s.marks)
        lowest = min(self.students, key=lambda s: s.marks)

        print("\n--- Statistics ---")
        print(f"Total Students : {total}")
        print(f"Average Marks  : {average:.2f}")
        print(f"Highest Marks  : {highest.name} ({highest.marks})")
        print(f"Lowest Marks   : {lowest.name} ({lowest.marks})")


def main():
    manager = StudentManager()

    while True:
        print("\n==============================")
        print("      STUDENT MANAGEMENT")
        print("==============================")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Statistics")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_student()

        elif choice == "2":
            manager.show_students()

        elif choice == "3":
            manager.search_student()

        elif choice == "4":
            manager.delete_student()

        elif choice == "5":
            manager.statistics()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
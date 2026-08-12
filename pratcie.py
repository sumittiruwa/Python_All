students = {
    "Ram": [80, 75, 90],
    "Shyam": [65, 70, 72],
    "Hari": [90, 88, 95]
}

for name, marks in students.items():
    average = sum(marks) / len(marks)

    print(name)
    print("Marks:", marks)
    print("Average:", average)
    print()
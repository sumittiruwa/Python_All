# using sorted 

students = [
    ("Krishna", 80),
    ("Subodh", 95),
    ("Sachin", 70)
]

sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)
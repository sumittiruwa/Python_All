""""5. Student Marks Statistics Generator 
Write a program that accepts marks of n students and calculates: 
● Highest mark 
● Lowest mark 
● Average mark 
Requirements: 
● Create separate functions for each task. 
● Use loops inside the functions. 
● Pass the marks list as an argu
ment. 
● Display all statistics.""""

def highest_mark(marks):
    highest = marks[0]
    for mark in marks:
        if mark > highest:
            highest = mark
    return highest

def lowest_mark(marks):
    lowest = marks[0]
    for mark in marks:
        if mark < lowest:
            lowest = mark
    return lowest

def average_mark(marks):
    total = 0
    for mark in marks:
        total += mark
    return total / len(marks)


n = int(input("Enter number of students: "))
marks = []

for i in range(n):
    mark = float(input(f"Enter marks of student {i + 1}: "))
    marks.append(mark)


print("Highest Mark:", highest_mark(marks))
print("Lowest Mark:", lowest_mark(marks))
print("Average Mark:", average_mark(marks))
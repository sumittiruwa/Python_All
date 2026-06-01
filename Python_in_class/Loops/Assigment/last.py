# 10. Student Performance Ranking System 
# Write a Python program that processes marks of multiple students. 
# Requirements: 
# ● Create a function that accepts a list of marks. 
# ● Use loops to calculate grades: 
# ○ A → 80 and above 
# ○ B → 60–79 
# ○ C → 40–59 
# ○ F → Below 40 
# ● Use a lambda function to sort marks in descending order. 
# ● Display: 
# ○ Sorted marks 
# ○ Grade distribution 
# ○ Number of passed students



# Function to assign grades and calculate statistics
def process_marks(marks):
    grade_count = {"A": 0, "B": 0, "C": 0, "F": 0}
    passed_students = 0  # A, B, C are considered pass

    # Assign grades using loop
    for mark in marks:
        if mark >= 80:
            grade_count["A"] += 1
            passed_students += 1
        elif 60 <= mark < 80:
            grade_count["B"] += 1
            passed_students += 1
        elif 40 <= mark < 60:
            grade_count["C"] += 1
            passed_students += 1
        else:
            grade_count["F"] += 1

    return grade_count, passed_students

# Input marks
n = int(input("Enter number of students: "))
marks = []

for i in range(n):
    mark = float(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

# Sort marks in descending order using lambda
sorted_marks = sorted(marks, key=lambda x: x, reverse=True)

# Process grades
grades, passed = process_marks(marks)

# Display results
print("\nSorted Marks:", sorted_marks)
print("Grade Distribution:", grades)
print("Number of Passed Students:", passed)
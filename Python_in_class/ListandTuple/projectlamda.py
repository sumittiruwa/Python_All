 # result analyzer using lamda 
 
students = [
    {"name": "Krishna", "marks": [90, 80, 70]},
    {"name": "Beta", "marks": [10, 20, 90]},
    {"name": "Sarita", "marks": [90, 90, 90]},
    {"name": "Sachin", "marks": [100, 99, 10]},
    {"name": "Bhupen", "marks": [60, 39, 90]},
    {"name": "Subodh", "marks": [90, 30, 25]},
    {"name": "Rahul", "marks": [10, 20, 80]}
]


#calculating total marks 

total_marks = list(map(lambda s: sum(s["marks"]), students))

# add and findinf average

for i, s in enumerate(students):
    s["total"] = total_marks[i]
    s["avg"] = s["total"]/len(s["marks"])
    
# assign grade using lamda

grade = lambda avg: "A" if avg >= 80 else "B" if avg >= 60 else "C"
for s in students:
    s["grade"] = grade(s["avg"])
    
# sort student by total 
sorted_students = sorted(students, key= lambda s: s["total"], reverse=True)

print("Sorted by Performance")

for s in sorted_students:
    print(s)

# filetring the top one

top_students = list(filter(lambda s: s["grade"] == "A", students))

print("\n tp students")

for s in top_students:
    print(s["name"])

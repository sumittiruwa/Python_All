#. Student Scholarship Eligibility System 
# Create a program that: 
# ● Takes student CGPA, attendance percentage, and number of backlogs as input. 
# ● Uses conditional statements to determine scholarship eligibility. 
# ● Rules: 
# ○ CGPA ≥ 3.7, attendance ≥ 85, backlogs = 0 → “Full Scholarship” 
# ○ CGPA ≥ 3.2 and attendance ≥ 75 → “Partial Scholarship” 
# ○ Otherwise → “Not Eligible” 
# ● Display all values with proper type casting and formatted output. 

student_name = input("Enter the student's name: ")
cgpa = float(input("Enter the student's CGPA: "))
attendance = float(input("Enter the student's attendance percentage: "))
backlogs = int(input("Enter the number of backlogs: "))

if cgpa >=3.7 and attendance >=85 and backlogs == 0:
    scholarship_status = "Full Scholarship"
elif cgpa >= 3.2 and attendance >= 75:
    scholarship_status = "Partial Scholarship"
else:
    scholarship_status = "Not Eligible"
print(f"Student Name: {student_name}")
print(f"CGPA: {cgpa:.2f}")  
print(f"Attendance: {attendance:.2f}%")
print(f"Backlogs: {backlogs}")
print(f"Scholarship Eligibility: {scholarship_status}")

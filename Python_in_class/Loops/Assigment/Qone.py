def count_eligible_students(attendance_list):
    count = 0
    for attendance in attendance_list:
        if attendance >= 75:
            count += 1
    return count


attendance_list = []

for i in range(10):
    attendance = float(input(f"Enter attendance percentage of student {i+1}: "))
    attendance_list.append(attendance)


eligible_students = count_eligible_students(attendance_list)


print("Number of students eligible (attendance >= 75%):", eligible_students)
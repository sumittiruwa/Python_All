import matplotlib.pyplot as plt


Students = ['Krishna','Sachin','Rahul','Bhupen','Sarita','Subodh']
Attendance = [90, 80, 70, 60, 50, 40]

plt.pie(Attendance, labels=Students, autopct='%1.1f%%', startangle=90)
plt.title("Student Attendance")
plt.show()
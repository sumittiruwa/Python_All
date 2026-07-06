import matplotlib.pyplot as plt

#aplt.sactter(x,y color='color_name', marker='marker style', s='size of marker')


Name = ['Krishna','Sachin','Rahul','Bhupen','Sarita','Subodh']
attendance = [90, 80, 70, 60, 50, 40]



plt.scatter(Name, attendance, color='red', marker='o', s=100)
plt.title("Student Attendance")
plt.xlabel("Students")
plt.ylabel("Attendance")
plt.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.7)
plt.show()
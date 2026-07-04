import matplotlib.pyplot as plt


Students = ['Krishna','Sachin','Rahul','Bhupen','Sarita','Subodh','Sushant','Anup','Mitsu']
Marks = [90, 80, 70, 60, 50, 40, 30, 20, 10]

plt.hist(Marks, bins=5, color='pink', edgecolor='black', alpha=0.7)
plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
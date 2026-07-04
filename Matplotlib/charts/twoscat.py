import matplotlib.pyplot as plt

# plt.scatter(x, y, color='color_name', marker='marker_style', s=size)

plt.scatter([1, 2, 3], [4, 5, 6], color='red', label='Class A')
plt.scatter([1, 2, 3], [7, 8, 9], color='blue', label='Class B')

plt.title("Student Attendance")
plt.xlabel("Student Number")
plt.ylabel("Attendance")
plt.legend('upper right')

plt.show()
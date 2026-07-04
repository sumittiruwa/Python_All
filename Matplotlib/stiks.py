import matplotlib.pyplot as plt

# plt.plot(x, y, color='color name', linestyle='line_style',
#          linewidth='width of line', marker='marker style',
#          markersize='size of marker')

months = [1, 2, 3, 4]
sales = [100, 200, 300, 400]

plt.plot(
    months,
    sales,
    color='green',
    linestyle='--',
    linewidth=2,
    marker='o',
    markersize=10
)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(color='gray', linestyle='-', linewidth=0.5, alpha=0.7)
plt.xlim(0, 5)
plt.ylim(0, 500)
plt.xticks([0, 1, 2, 3, 4, 5],['0', 'Jan', 'Feb', 'Mar', 'Apr', 'May'])
plt.yticks([0, 100, 200, 300, 400, 500],['0', '100', '200', '300', '400', '500'])
plt.show()
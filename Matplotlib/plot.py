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

plt.show()
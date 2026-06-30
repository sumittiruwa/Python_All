import matplotlib.pyplot as plt
import numpy as np

# Generate Data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create Figure
plt.figure(figsize=(12, 7))

# Plot Graphs
plt.plot(
    x, y1,
    color="blue",
    linewidth=3,
    linestyle="-",
    marker="o",
    markersize=5,
    markevery=10,
    label="sin(x)"
)

plt.plot(
    x, y2,
    color="red",
    linewidth=3,
    linestyle="--",
    marker="s",
    markersize=5,
    markevery=10,
    label="cos(x)"
)

# Fill Area
plt.fill_between(x, y1, alpha=0.2)

# Grid
plt.grid(True, linestyle="--", alpha=0.7)

# Labels
plt.title("Advanced Matplotlib Graph", fontsize=20)
plt.xlabel("X Values", fontsize=14)
plt.ylabel("Y Values", fontsize=14)

# Axis Limits
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

# Ticks
plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(-1.5, 1.6, 0.5))

# Legend
plt.legend(loc="upper right", fontsize=12)

# Annotation
plt.annotate(
    "Maximum",
    xy=(1.57, 1),
    xytext=(3, 1.3),
    arrowprops=dict(facecolor="black", shrink=0.05),
)

# Horizontal and Vertical Lines
plt.axhline(0, color="black", linewidth=1)
plt.axvline(5, color="green", linestyle=":")

# Text
plt.text(7, -1.2, "Matplotlib Demo", fontsize=12)

plt.tight_layout()
plt.show()
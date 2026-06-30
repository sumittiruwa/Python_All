import matplotlib.pyplot as plt

x = ["Mon", "Tue", "Wed", "Thu"]
y = [10,90,30,70]

plt.plot(x,y)
plt.title("Cafe Sales of this week")

plt.xlabel("Day of the week")
plt.ylabel("Sales per day")
plt.show()
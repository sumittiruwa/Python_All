import matplotlib.pyplot as plt

product = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [100, 200, 300, 400]

plt.barh(product, sales, color='blue', height=0.5)

plt.title("Product Sales")
plt.xlabel("Sales")
plt.ylabel("Products")
plt.legend(['Sales'], loc='lower right')

plt.show()
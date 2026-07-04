import matplotlib.pyplot as plt




product = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [100, 200, 300, 400]
plt.bar(product, sales, color='blue', width=0.5)
plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.legend(['Sales'], loc='upper left')
plt.show()
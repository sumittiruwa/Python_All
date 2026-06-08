# #slicing


# array[satrt:stop:step]


import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(arr[1,5])  # Output: [20 30 40 50]
print(arr[:4])
print(arr[::2]) # Output: [10 30 50 70 90]
print(arr[::-1]) # Output: [90 80 70 60 50 40 30 20 10] 
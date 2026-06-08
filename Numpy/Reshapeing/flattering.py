"""
multi dimensional array can be reshaped into one dimensional array using flatten() method"""



import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
flattened_arr = arr.flatten()
print(flattened_arr)
# reshape (rows, columns) speification to change the shape of an array. It returns a new array with the specified shape, while keeping the original data intact. The total number of elements in the new shape must be the same as in the original array.
# only when dimesnion matches then only reshape will work otherwise it will give error.




import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_arr = arr.reshape(2, 3)
print(reshaped_arr)
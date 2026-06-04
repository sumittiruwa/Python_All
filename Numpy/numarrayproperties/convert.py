# converting the datatype 


import numpy as np

ar = np.array([1,2,3,4,5])
print(ar.dtype)
ar_float = ar.astype(np.float64)
print(ar_float)
print(ar_float.dtype)


name = np.array(['sumit','krishna','manish','satyarth'])
print(name.dtype)
name_int = name.astype(np.int32)
print(name_int)
print(name_int.dtype)
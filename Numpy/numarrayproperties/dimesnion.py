# number of dimesnions in the array 

import numpy as np

ar = np.array([[1,2,3],[4,5,6],[7,8,9]])
ar1 = np.array([1,2,3,4,5])
ar2 = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]])   
print(ar.ndim)
print(ar1.ndim)
print(ar2.ndim)
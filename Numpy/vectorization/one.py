import numpy as np

list1 = [1,2,3]
list2 = [3,4,5]

result = [x+y for x,y in zip(list1,list2)]
print(result)
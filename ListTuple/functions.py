#List Methods
# -it work like functions but work on list
# -it is used to perform specific operation on list 

list = [1, 2, 3, 4, 5]

list.append(6) # it will add 6 at the end of the list
print(list) # it will print [1, 2, 3, 4, 5, 6]
list.sort() # it will sort the list in ascending order
print(list) # it will print [1, 2, 3, 4,    
list.reverse() # it will reverse the list
print(list) # it will print [6, 5, 4, 3,
list.insert(0, 0) # it will insert 0 at index 0
print(list) # it will print [0, 6, 5, 4,
list.remove(6) # it will remove 6 from the list
print(list) # it will print [0, 5, 4, 3,
list.pop() # it will remove the last element from the list
print(list) # it will print [0, 5, 4, 3]
list.clear() # it will remove all the elements from the list
print(list) # it will print []  
list.extend([1, 2, 3]) # it will add the elements of the list to the end of the list
print(list) # it will print [1, 2, 3]
list.count(2) # it will count the number of times 2 is present in the list
print(list.count(2)) # it will print 1
list.index(2) # it will return the index of the first occurrence of 2 in the list
print(list.index(2)) # it will print 1  
list.copy() # it will return a copy of the list
new_list = list.copy() # it will create a new list with the same elements as the    
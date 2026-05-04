# data type that store set  of values


makrs = [90, 80, 70, 60, 50]
print(makrs)
print(makrs[0]) # it will print 90
print(makrs[1]) # it will print 80          
print(makrs[2]) # it will print 70
print(makrs[3]) # it will print 60

# list is mutable
makrs[0] = 95   

print(makrs) # it will print [95, 80, 70, 60, 50]

print(type(makrs)) # it will print <class 'list'>
print(len(makrs)) # it will print 5


#you can store different data type in a list
my_list = [1, "hello", 3.14, True]
print(my_list)
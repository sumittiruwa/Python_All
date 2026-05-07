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


# immutable  - string  (can't change the value of string)
#muttable - list (can change the value of list)


student = ("mitsu" , 23, "bhatktapur")
print(student)
print(student[0]) # it will print mitsu
print(student[1]) # it will print 23
print(student[2]) # it will print bhatktapur

student[0] = "ram" # it will give error because tuple is immutable  
print(student)
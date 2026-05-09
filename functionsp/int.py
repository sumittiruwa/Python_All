# def cal_sum(a, b):
#     sum = a + b
#     print(f"The sum of {a} and {b} is: {sum}")      
#     return a + b



def greet():
    print("Hello World")

greet()


def sum(a, b):
    s = a + b
    return s

print(sum(5, 10))

#build in function
print(len("Hello World")) # it will print the length of the string
print(type(5)) # it will print the type of the variable 
print(type("Hello World")) # it will print the type of the variable
print(type(5.5)) # it will print the type of the variable
print(type(True)) # it will print the type of the variable


def calc( a=1 , b= 2):
    return a + b
print(calc()) # it will print 3
print(calc(5)) # it will print 7
print(calc(5, 10)) # it will print 15
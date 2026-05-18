# class name:
#     x = 5

# p1 = name()
# print(p1.x)

# del p1

# class Student:
#     name ="devil"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

#class created
class Car:
    color = "blue"
    model = "BMW"
#object created
car1 = Car()
print(car1.color)
print(car1.model)


#--init_-_function  auto call when object created
class Person:
    def __init__(self):
        print("This is a constructor")
        
p1 = Person()
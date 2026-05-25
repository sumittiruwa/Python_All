# Access Modifier
# Private members are accessible only within the class

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display_info(self):
        print(f"The person name is {self.__name} and the age is {self.__age}")


p1 = Person("Sumit", 20)
p1.display_info()
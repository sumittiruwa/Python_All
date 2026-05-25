#access modifier
#private - are those method which is only accesble within a class 
#constructor
class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def display_info(self):
        print(f"the person name is {self.__name}and the age is  {self.__age}")
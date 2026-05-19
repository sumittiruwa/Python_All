class Student:
    def __init__(self, name):
        self.name = name

        s1 = Student("ravan")
        print(s1.name)
        del s1
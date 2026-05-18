class Student:
    def __init__ (self, name, marks): 
                                       self.name = name
                                       self.marks = marks
                                       def get_avg(self):
                                               sum = 0
                                               for val in self.marks.values():
                                                       sum += val
                                                       print ("hi,", self.name, "your average marks is", sum/len(self.marks))

                                                       s1.get_avg()
s1 = Student("tony stark", 90) 
# Class

class Student:
    def __init__(self, name, score):
        self.name = name      # Attribute
        self.score = score

    def grade(self):          # Method
        return "A" if self.score >= 90 else "B"

# Create objects

s1 = Student("Ram", 90)
s2 = Student("Sam", 78)

print(s1.name, s1.grade())
print(s2.name, s2.grade())
print(type(s1))
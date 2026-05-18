class Car:
    def __init__(self):
        self.acc = False 
        self.brk = False
        self.steering = False
    def start(self):
        self.acc = True
        self.brk = True
        self.steering = False

c1 = Car()
print(c1.acc)
print(c1.brk)
print(c1.steering)
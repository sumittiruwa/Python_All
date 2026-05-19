class Car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")


class BMW(Car):
    def __init__(self, name):
        self.name = name


car1 = BMW("sedan")
car2 = BMW("SUV")

car1.start()
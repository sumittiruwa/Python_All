class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Woof")

    def fetch(self):
        return f"{self.name} fetches the ball!"


class GuideDog(Dog):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner

    def guide(self):
        return f"{self.name} guides {self.owner}"


gd = GuideDog("Rex", "Krishna")

print(gd.speak())
print(gd.fetch())
print(gd.guide())
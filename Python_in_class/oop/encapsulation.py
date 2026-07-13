class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner          # Public
        self._bank = "Siddharth"    # Protected
        self.__balance = balance    # Private

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"{self.owner}: Rs. {self.__balance}"


acc = BankAccount("Krishna", 100000)

acc.deposit(20000)

print(acc.get_balance())

print(acc.owner)         # Public attribute
# print(acc.__balance)   # Error: Private attribute

print(acc._BankAccount__balance)  # Accessing private attribute (not recommended)

print(acc)
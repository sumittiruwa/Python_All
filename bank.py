from abc import ABC, abstractmethod
import json
import os

class BankError(Exception):
    pass

class InsufficientBalance(BankError):
    pass

class AccountNotFound(BankError):
    pass

class Account(ABC):
    def __init__(self, number, name, balance):
        self._number = number
        self._name = name
        self._balance = balance

    @property
    def number(self):
        return self._number

    @property
    def balance(self):
        return self._balance

    @abstractmethod
    def account_type(self):
        pass

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientBalance("Insufficient Balance")
        self._balance -= amount

    def __add__(self, amount):
        self.deposit(amount)
        return self

    def __sub__(self, amount):
        self.withdraw(amount)
        return self

    def to_dict(self):
        return {
            "type": self.account_type(),
            "number": self._number,
            "name": self._name,
            "balance": self._balance
        }

class SavingsAccount(Account):
    def account_type(self):
        return "Savings"

class CurrentAccount(Account):
    def account_type(self):
        return "Current"

class Bank:
    def __init__(self, file="bank.json"):
        self.file = file
        self.accounts = {}
        self.load()

    def create(self, account):
        self.accounts[account.number] = account
        self.save()

    def delete(self, number):
        if number not in self.accounts:
            raise AccountNotFound("Account Not Found")
        del self.accounts[number]
        self.save()

    def search(self, number):
        if number not in self.accounts:
            raise AccountNotFound("Account Not Found")
        return self.accounts[number]

    def transfer(self, sender, receiver, amount):
        s = self.search(sender)
        r = self.search(receiver)
        s.withdraw(amount)
        r.deposit(amount)
        self.save()

    def display(self):
        if not self.accounts:
            print("No Accounts")
            return
        for acc in self.accounts.values():
            print(
                acc.number,
                acc._name,
                acc.account_type(),
                acc.balance
            )

    def save(self):
        data = [a.to_dict() for a in self.accounts.values()]
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4)

    def load(self):
        if not os.path.exists(self.file):
            return
        with open(self.file) as f:
            data = json.load(f)
            for d in data:
                if d["type"] == "Savings":
                    acc = SavingsAccount(
                        d["number"],
                        d["name"],
                        d["balance"]
                    )
                else:
                    acc = CurrentAccount(
                        d["number"],
                        d["name"],
                        d["balance"]
                    )
                self.accounts[acc.number] = acc

bank = Bank()

while True:
    print("\n1.Create")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Transfer")
    print("5.Search")
    print("6.Display")
    print("7.Delete")
    print("8.Exit")

    ch = input("Choice: ")

    try:
        if ch == "1":
            n = input("Account Number: ")
            name = input("Name: ")
            b = float(input("Balance: "))
            t = input("Type(S/C): ").upper()

            if t == "S":
                bank.create(SavingsAccount(n, name, b))
            else:
                bank.create(CurrentAccount(n, name, b))

        elif ch == "2":
            acc = bank.search(input("Account Number: "))
            acc + float(input("Amount: "))
            bank.save()

        elif ch == "3":
            acc = bank.search(input("Account Number: "))
            acc - float(input("Amount: "))
            bank.save()

        elif ch == "4":
            s = input("Sender: ")
            r = input("Receiver: ")
            a = float(input("Amount: "))
            bank.transfer(s, r, a)

        elif ch == "5":
            acc = bank.search(input("Account Number: "))
            print(
                acc.number,
                acc._name,
                acc.account_type(),
                acc.balance
            )

        elif ch == "6":
            bank.display()

        elif ch == "7":
            bank.delete(input("Account Number: "))

        elif ch == "8":
            break

        else:
            print("Invalid Choice")

    except Exception as e:
        print(e)
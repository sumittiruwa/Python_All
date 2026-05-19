class Account:
    def __init__(self, bal, acc_no):
        self.balance = bal
        self.account_number = acc_no

def debit(self, amount):
    if self.balance >= amount:
        self.balance -= amount
        print(f"Debited {amount}. New balance: {self.balance}")
        print("total balance:", self.balance)
    else:
        print("Insufficient funds")

def credit(self, amount):
    self.balance += amount
    print(f"Credited {amount}. New balance: {self.balance}")

def get_balance(self):
    return self.balance

acc1 = Account(1000, 12345)
print(acc1.balance)
print(acc1.account_number)

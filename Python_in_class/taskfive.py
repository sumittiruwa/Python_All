marks = 10
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")

balance = 5000
withdrawal_amount = 6000

if withdrawal_amount > balance:
    print("Insufficient funds")     
else:    balance -= withdrawal_amount
print(f"Withdrawal successful. Remaining balance: {balance}")   


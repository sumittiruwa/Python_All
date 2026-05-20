# ake integer N from user. Use a for loop to calculate 1+2+...+N. Print the sum.

num = int(input("Enter an integer: "))
total = 0
for i in range(1, num + 1):
    total += i
print("The sum is:", total)
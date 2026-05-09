#program to print the length of the list
cities = ["kathmandu", "bhaktapur", "lalitpur"]
heroes = ["naruto", "sasuke", "sakura"]

def print_length(lst):
    print(len(lst))
print_length(cities)

print_length(cities)
print_length(heroes)



print(heroes[0], end ="\n") # it will print naruto
print(heroes[1], end ="\n") # it will print sasuke
print(heroes[2]) # it will print sakura



# program to find the factorial of a number

n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print(f"The factorial of {n} is: {fact}")


# by function
def factorial(n):
    fact = 1
    for i in range(1, 1+n):
        fact *= i
        return fact
    print(factorial(5))
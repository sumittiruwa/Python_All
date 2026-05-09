# a functions that calls itself is called a recursive function. It is used to solve problems that can be broken down into smaller, similar problems. The main advantage of using recursion is that it can simplify code and make it easier to read. 

def show(n):
    print(n)

show(5) # it will print 5


# using recursion 

def show(n):
    print(n)  
    show(n-1) # it will call the function again with n-1  


def show(n):
    if n == 0:
        return

    print(n)
    show(n-1)

show(1000) # it will print 5, 4, 3, 2, 1


def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n-1)   


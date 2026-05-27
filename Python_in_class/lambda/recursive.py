# factorail - class recursion 

def factorial(n):
    if n == 0:
        return 1 
    return n* factorial(n-1)

#fibonacci -tree recursion
def fib(n):
    if n  <= 1:
        return n 
    return fib(n-1) + fib(n-2) #recursive case
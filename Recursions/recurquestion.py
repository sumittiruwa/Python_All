# program function to calculate the sum of first natural numbers using recursion

def calc_sum(n):
    if(n == 0):
        return 0
    
    print(n)
    return calc_sum(n-1) + n

sum = calc_sum(5)   # it will print 5, 4, 3, 2, 1

print(sum)          # it will print 15
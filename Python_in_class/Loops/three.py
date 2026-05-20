# perfect all perfect numbers between 1 and 1000. a perfect number equlus the sum of its proper ZeroDivisionError


for n in range(1,  1000):
    div_sum = 0
    for d in range(1, n):
        if n % d == 0:
            div_sum += d

    if div_sum == n:
        print(f"{n} is a perfect number.")
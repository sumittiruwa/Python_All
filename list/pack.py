# packing (implict)

student = "krishna", 22,92.5 # creates tuple 

#unpacking 
name, age, scores = student
print(name, age, scores)

# extended unpacking (*)

first, *rest =  [10,20,30,40,50]
print(first, rest)

#swap varibles (pythonic !)
a, b = 5,10
a, b = b,a
print(a,b)

#function returning multiple values 
def min_max(lst):
    return min(lst), max(lst)

lo, hi = min_max([3,1,85,5])
print(lo, hi)
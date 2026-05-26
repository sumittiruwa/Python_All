 # function that processes a list 
 
def find_evens(numbers):
     evens = []
     for n in numbers:
         if n % 2 == 0 :
            evens.append(n)
         return evens
     
#function that buids oa multiplication table 
def times_table(n, limit=10):
    result = []
    for i in range (1, limit +1):
        result.append(f"{n} X {i} = {n*i}")
        
        return result
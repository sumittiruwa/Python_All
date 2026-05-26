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
    
    
# functions with loops adn lists

def flatten(nested):
    flat = []
    for sublist in nested:
        for item in sublist:
            flat.append(item)
            
            return flat
        
data = [1,2,3,4,5,6,7,8]
matrix = [[1,2,3], [2,3,4], [3,4,5]]

print(find_evens(data))
print(times_table(3,5))
print(flatten(matrix))
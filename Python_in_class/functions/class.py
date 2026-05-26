# def function_nmae(param1, param2):
#     the function return result


def calculated_area(length, width):
    area = length * width
    return area

#calling the function 

result = calculated_area(8, 5)
print(f"{result}")


# Types of function arguments

#1 . positional

def add(a,b):
    return a+b
print(add(3,5))

# default

def greet(name, msg="hi"):
    print(f"{msg}, {name}!")
    
    greet("krishna ji ")
    greet("subodh", "bye")
    
# keyword 

def info(name, age, city):
    print(f"{name}, {age}, {city}")
    
    info(age = 25, city = "kathmandu", name = "krihsna")
    
    
#args / ** kwargs



def total(*nums):
    return sum(nums)

def show(**info):
    for k,v in info.items():
        print(f"{k}:{v}")
# varibles scope - local  vs global 

x = 5 # global - visible everywhere 

def show_scope():
    y = 200    #local - only inside this function
    print(f"inside: x ={x}, y={y}")     # can see global x


def modify_global():
    global x # declare intent to modify global 
    
    k = 999
    print(f"modified  x to {x}")  # x change the varible
    
show_scope()
modify_global()
print(f"outside: x = {x}")  # x chnaged globally 


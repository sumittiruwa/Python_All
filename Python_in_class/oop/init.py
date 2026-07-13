class Product:
    # class variale - shred by all instance
    
    discount = 0.10
    
    def __init__(self, name, price, category="General"):
        self.name = name # insactce var
        self.price = price 
        self.category = category
        
    def final_price(self):
        return self.price * ( 1 - Product.discount)
    def __str__(self):
        return f"{self.name} - Rs.{self.final_price():.0f}"
p1 = Product("krishmna", 80000, "OldMonk")
p2 = Product("Subodh", 20 , "Ice") 
print(p1)
print(p2.category)
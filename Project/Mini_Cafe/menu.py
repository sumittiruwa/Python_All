#dicstornary data type

menu = {
    "coffee": 100,
    "tea": 50,  
    "momo": 150,
    "pizza": 500,
    "burger": 200
}

print("welcome to devil cafe")
print("Pizza: 500\nBurger: 200\nMomo: 150\nTea: 50\nCoffee: 100")


order_total =0

item_1 = input("Enter your first item: ")
 
if item_1 in menu:
    order_total += menu[item_1]

    print(f"{item_1} added to your order. Price: {menu[item_1]}")
else:
    print(f"Sorry, {item_1}  not in my cafe , go to another cafe.")   

another_item = input("Do you want to order another item? (yes/no): ")   
 
if another_item == "yes":
    item_2 = input("Enter your second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2} added to your order. Price: {menu[item_2]}")
    else:
        print(f"Sorry, {item_2} not in my cafe , go to another cafe.")

print(f"Your total order amount is: {order_total}")
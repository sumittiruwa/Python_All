#rRent Calculator

rent = int(input("enter the rent amt:"))
food = int(input("enter the food expenses:"))
people = int(input("enter the number of people:"))
electricity = int(input("enter the electricity bill:"))
charge_per_unit = int(input("enter the charge per unit of electricity:"))
total_electricity = electricity * charge_per_unit
total_expenses = rent + food + total_electricity
per_person_expense = total_expenses / people
print(f"Total expenses: {total_expenses}")
print(f"Each person should pay: {per_person_expense:.2f}")
print(f"Rent: {rent}, Food: {food}, Electricity: {total_electricity}, People: {people}")

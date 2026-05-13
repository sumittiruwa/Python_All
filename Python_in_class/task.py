total_bills = 3750.00
number_of_people = 5
paid_extra = True
discount = 10
name = "Sumit"

total = total_bills - total_bills * discount / 100

average_bill = total / number_of_people

print(f"Total bill after discount: {total}")
print(f"Average bill per person: {average_bill}")

print(type(total_bills))
print(type(number_of_people))
print(type(paid_extra))
print(type(discount))
print(type(name))
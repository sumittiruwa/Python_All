name = input("Enter your name: ")
weight = float(input)("Enter your weight in kg: ")
height = float(input)("Enter your height in m: ")

bmi = float(weight) / (float(height) ** 2)
print(f"Your BMI is: {bmi:.2f}")

if weight < 18.5:
    print("You are underweight.")
elif 18.5 <= weight < 24.9:
    print("You have a normal weight.")
elif 25 <= weight < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")


print(f"Name: {name}, Weight: {weight}, Height: {height}")
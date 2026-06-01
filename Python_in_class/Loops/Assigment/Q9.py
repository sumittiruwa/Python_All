# Recursive function to calculate computational cost
def calculate_cost(n):
    if n == 1:  # Base case
        return 1
    return calculate_cost(n - 1) + n**2

# Input number of layers
layers = int(input("Enter number of layers: "))

# Calculate and display cost
cost = calculate_cost(layers)

print("Total Computational Cost:", cost)
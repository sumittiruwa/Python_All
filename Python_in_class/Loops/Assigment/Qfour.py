
def learning_rate_decay(current_rate, iterations):
    if iterations == 0:  # Base case
        return current_rate
    return learning_rate_decay(current_rate * 0.9, iterations - 1)

initial_rate = float(input("Enter initial learning rate: "))
n = int(input("Enter number of iterations: "))


final_rate = learning_rate_decay(initial_rate, n)


print("Final learning rate:", final_rate)
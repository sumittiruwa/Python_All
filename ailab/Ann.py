def perceptron(x1, x2, weights, bias):
    total = x1 * weights[0] + x2 * weights[1] + bias

    if total >= 0:
        return 1
    else:
        return 0


# Input values
inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

# AND Gate
print("AND Gate")
for x1, x2 in inputs:
    print(x1, x2, "->", perceptron(x1, x2, [1, 1], -1.5))


# OR Gate
print("\nOR Gate")
for x1, x2 in inputs:
    print(x1, x2, "->", perceptron(x1, x2, [1, 1], -0.5))


# NOT Gate
print("\nNOT Gate")
for x in [0, 1]:
    total = x * -1 + 0.5
    output = 1 if total >= 0 else 0
    print(x, "->", output)
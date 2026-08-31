"""ML Practice: Common Neural Network Activation Functions"""

import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def relu(x):
    return max(0, x)


def leaky_relu(x, alpha=0.01):
    return x if x > 0 else alpha * x


def tanh(x):
    return math.tanh(x)


def softmax(values):
    max_val = max(values)
    exps = [math.exp(v - max_val) for v in values]
    total = sum(exps)
    return [e / total for e in exps]


if __name__ == "__main__":
    inputs = [-2, -1, 0, 1, 2]

    print("Sigmoid:", [round(sigmoid(x), 4) for x in inputs])
    print("ReLU:", [relu(x) for x in inputs])
    print("Leaky ReLU:", [round(leaky_relu(x), 4) for x in inputs])
    print("Tanh:", [round(tanh(x), 4) for x in inputs])
    print("Softmax:", [round(v, 4) for v in softmax(inputs)])

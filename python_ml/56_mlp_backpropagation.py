"""ML Practice: 2-Layer MLP Trained with Backpropagation on XOR"""

import math
import random


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def sigmoid_deriv(a):
    return a * (1 - a)


def init_weights(n_in, n_hidden, seed=1):
    random.seed(seed)
    w1 = [[random.uniform(-1, 1) for _ in range(n_in)] for _ in range(n_hidden)]
    b1 = [0.0] * n_hidden
    w2 = [random.uniform(-1, 1) for _ in range(n_hidden)]
    b2 = 0.0
    return w1, b1, w2, b2


def forward(x, w1, b1, w2, b2):
    hidden = [sigmoid(sum(w * xi for w, xi in zip(neuron, x)) + b) for neuron, b in zip(w1, b1)]
    output = sigmoid(sum(w * h for w, h in zip(w2, hidden)) + b2)
    return hidden, output


def train(X, y, n_hidden=4, lr=0.5, epochs=5000, seed=1):
    w1, b1, w2, b2 = init_weights(len(X[0]), n_hidden, seed)

    for _ in range(epochs):
        for x, target in zip(X, y):
            hidden, output = forward(x, w1, b1, w2, b2)

            output_error = output - target
            output_delta = output_error * sigmoid_deriv(output)

            hidden_deltas = [output_delta * w2[i] * sigmoid_deriv(hidden[i]) for i in range(n_hidden)]

            for i in range(n_hidden):
                w2[i] -= lr * output_delta * hidden[i]
            b2 -= lr * output_delta

            for i in range(n_hidden):
                for j in range(len(x)):
                    w1[i][j] -= lr * hidden_deltas[i] * x[j]
                b1[i] -= lr * hidden_deltas[i]

    return w1, b1, w2, b2


if __name__ == "__main__":
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y = [0, 1, 1, 0]

    w1, b1, w2, b2 = train(X, y)

    for x, target in zip(X, y):
        _, output = forward(x, w1, b1, w2, b2)
        print(f"{x} -> predicted={output:.3f}, target={target}")

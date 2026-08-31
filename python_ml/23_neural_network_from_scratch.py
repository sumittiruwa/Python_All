"""ML Practice: Simple Feedforward Neural Network (1 hidden layer, from scratch)"""

import math
import random


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def sigmoid_derivative(output):
    return output * (1 - output)


class NeuralNetwork:
    def __init__(self, n_input, n_hidden, n_output, seed=1):
        random.seed(seed)
        self.w1 = [[random.uniform(-1, 1) for _ in range(n_input)] for _ in range(n_hidden)]
        self.b1 = [0.0] * n_hidden
        self.w2 = [[random.uniform(-1, 1) for _ in range(n_hidden)] for _ in range(n_output)]
        self.b2 = [0.0] * n_output

    def forward(self, x):
        hidden = [sigmoid(sum(self.w1[h][i] * x[i] for i in range(len(x))) + self.b1[h]) for h in range(len(self.w1))]
        output = [sigmoid(sum(self.w2[o][h] * hidden[h] for h in range(len(hidden))) + self.b2[o]) for o in range(len(self.w2))]
        return hidden, output

    def train(self, X, y, lr=0.5, epochs=5000):
        for _ in range(epochs):
            for x, target in zip(X, y):
                hidden, output = self.forward(x)

                output_errors = [(target[o] - output[o]) * sigmoid_derivative(output[o]) for o in range(len(output))]
                hidden_errors = [
                    sum(output_errors[o] * self.w2[o][h] for o in range(len(output))) * sigmoid_derivative(hidden[h])
                    for h in range(len(hidden))
                ]

                for o in range(len(self.w2)):
                    for h in range(len(hidden)):
                        self.w2[o][h] += lr * output_errors[o] * hidden[h]
                    self.b2[o] += lr * output_errors[o]

                for h in range(len(self.w1)):
                    for i in range(len(x)):
                        self.w1[h][i] += lr * hidden_errors[h] * x[i]
                    self.b1[h] += lr * hidden_errors[h]

    def predict(self, x):
        _, output = self.forward(x)
        return output


if __name__ == "__main__":
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y = [[0], [1], [1], [0]]  # XOR

    nn = NeuralNetwork(n_input=2, n_hidden=4, n_output=1)
    nn.train(X, y)

    for x in X:
        print(f"Input {x} -> Output {round(nn.predict(x)[0], 3)}")

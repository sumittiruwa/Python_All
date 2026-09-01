"""ML Practice: Logistic Regression with L2 (Ridge) Regularization"""

import math


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def train(X, y, lr=0.1, lam=0.1, epochs=500):
    n_features = len(X[0])
    weights = [0.0] * n_features
    bias = 0.0
    n = len(X)

    for _ in range(epochs):
        grad_w = [0.0] * n_features
        grad_b = 0.0

        for xi, yi in zip(X, y):
            pred = sigmoid(sum(w * x for w, x in zip(weights, xi)) + bias)
            error = pred - yi
            for j in range(n_features):
                grad_w[j] += error * xi[j]
            grad_b += error

        for j in range(n_features):
            weights[j] -= lr * (grad_w[j] / n + lam * weights[j])
        bias -= lr * (grad_b / n)

    return weights, bias


def predict(x, weights, bias):
    prob = sigmoid(sum(w * xi for w, xi in zip(weights, x)) + bias)
    return 1 if prob >= 0.5 else 0, prob


if __name__ == "__main__":
    X = [[2.0, 1.0], [3.0, 2.0], [1.0, 0.5], [6.0, 5.0], [7.0, 6.0], [5.5, 5.5]]
    y = [0, 0, 0, 1, 1, 1]

    weights, bias = train(X, y)
    print("Weights:", [round(w, 3) for w in weights], "Bias:", round(bias, 3))

    for x in [[1.5, 1.0], [6.5, 6.0]]:
        label, prob = predict(x, weights, bias)
        print(f"{x} -> class {label} (prob={prob:.3f})")

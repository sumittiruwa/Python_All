"""ML Practice: Logistic Regression for Binary Classification"""

import math


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def train(X, y, lr=0.1, epochs=2000):
    n_samples = len(X)
    n_features = len(X[0])
    weights = [0.0] * n_features
    bias = 0.0

    for _ in range(epochs):
        y_pred = [sigmoid(sum(weights[j] * X[i][j] for j in range(n_features)) + bias) for i in range(n_samples)]
        errors = [y_pred[i] - y[i] for i in range(n_samples)]

        for j in range(n_features):
            grad_w = (1 / n_samples) * sum(errors[i] * X[i][j] for i in range(n_samples))
            weights[j] -= lr * grad_w

        grad_b = (1 / n_samples) * sum(errors)
        bias -= lr * grad_b

    return weights, bias


def predict(X, weights, bias, threshold=0.5):
    probs = [sigmoid(sum(weights[j] * row[j] for j in range(len(weights))) + bias) for row in X]
    return [1 if p >= threshold else 0 for p in probs]


if __name__ == "__main__":
    X = [[1], [2], [3], [6], [7], [8]]
    y = [0, 0, 0, 1, 1, 1]

    weights, bias = train(X, y)
    print("Weights:", [round(w, 3) for w in weights], "Bias:", round(bias, 3))
    print("Predictions:", predict(X, weights, bias))

"""ML Practice: Stochastic Gradient Descent Linear Classifier"""

import random


def train_sgd(X, y, lr=0.01, epochs=50, seed=1):
    random.seed(seed)
    n_features = len(X[0])
    weights = [0.0] * n_features
    bias = 0.0
    indices = list(range(len(X)))

    for _ in range(epochs):
        random.shuffle(indices)
        for i in indices:
            xi, yi = X[i], y[i]
            margin = yi * (sum(w * x for w, x in zip(weights, xi)) + bias)
            if margin < 1:
                for j in range(n_features):
                    weights[j] += lr * (yi * xi[j])
                bias += lr * yi

    return weights, bias


def predict(x, weights, bias):
    score = sum(w * xi for w, xi in zip(weights, x)) + bias
    return 1 if score >= 0 else -1


if __name__ == "__main__":
    X = [[1, 2], [2, 1], [2, 3], [8, 8], [9, 7], [7, 9]]
    y = [-1, -1, -1, 1, 1, 1]

    weights, bias = train_sgd(X, y)
    print("Weights:", [round(w, 3) for w in weights], "Bias:", round(bias, 3))

    for x in [[1.5, 1.5], [8.5, 8.5]]:
        print(f"{x} -> class {predict(x, weights, bias)}")

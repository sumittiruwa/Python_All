"""ML Practice: Softmax Regression for Multiclass Classification"""

import math


def softmax(scores):
    max_score = max(scores)
    exps = [math.exp(s - max_score) for s in scores]
    total = sum(exps)
    return [e / total for e in exps]


def train(X, y, n_classes, lr=0.1, epochs=1000):
    n_samples = len(X)
    n_features = len(X[0])
    weights = [[0.0] * n_features for _ in range(n_classes)]
    bias = [0.0] * n_classes

    for _ in range(epochs):
        for i in range(n_samples):
            scores = [sum(weights[c][j] * X[i][j] for j in range(n_features)) + bias[c] for c in range(n_classes)]
            probs = softmax(scores)

            for c in range(n_classes):
                target = 1 if y[i] == c else 0
                error = probs[c] - target
                for j in range(n_features):
                    weights[c][j] -= lr * error * X[i][j]
                bias[c] -= lr * error

    return weights, bias


def predict(X, weights, bias, n_classes):
    predictions = []
    for row in X:
        scores = [sum(weights[c][j] * row[j] for j in range(len(row))) + bias[c] for c in range(n_classes)]
        probs = softmax(scores)
        predictions.append(probs.index(max(probs)))
    return predictions


if __name__ == "__main__":
    X = [[1, 1], [2, 1], [4, 5], [5, 5], [8, 1], [9, 2]]
    y = [0, 0, 1, 1, 2, 2]

    weights, bias = train(X, y, n_classes=3)
    print("Predictions:", predict(X, weights, bias, n_classes=3))

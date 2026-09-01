"""ML Practice: Kernel SVM (RBF kernel) Binary Classification"""

import math


def rbf_kernel(a, b, gamma=0.5):
    sq_dist = sum((a[i] - b[i]) ** 2 for i in range(len(a)))
    return math.exp(-gamma * sq_dist)


def train_kernel_perceptron(X, y, gamma=0.5, epochs=20):
    n = len(X)
    alphas = [0.0] * n
    bias = 0.0

    for _ in range(epochs):
        for i in range(n):
            score = sum(alphas[j] * y[j] * rbf_kernel(X[j], X[i], gamma) for j in range(n)) + bias
            if y[i] * score <= 0:
                alphas[i] += 1.0
                bias += y[i]

    return alphas, bias


def predict(X, y, alphas, bias, x, gamma=0.5):
    score = sum(alphas[j] * y[j] * rbf_kernel(X[j], x, gamma) for j in range(len(X))) + bias
    return 1 if score >= 0 else -1


if __name__ == "__main__":
    X = [[0, 0], [0.2, 0.1], [0.1, -0.1], [1, 1], [1.2, 0.9], [0.9, 1.1], [-1, -1], [-1.2, -0.8]]
    y = [1, 1, 1, -1, -1, -1, 1, 1]

    alphas, bias = train_kernel_perceptron(X, y, gamma=0.7)

    for point in [[0.05, 0.0], [1.1, 1.0], [-1.1, -0.9]]:
        print(f"{point} -> class {predict(X, y, alphas, bias, point, gamma=0.7)}")

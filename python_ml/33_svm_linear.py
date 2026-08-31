"""ML Practice: Linear Support Vector Machine using Gradient Descent (hinge loss)"""


def train(X, y, lr=0.001, epochs=1000, C=1.0):
    n_samples = len(X)
    n_features = len(X[0])
    weights = [0.0] * n_features
    bias = 0.0

    for _ in range(epochs):
        for i in range(n_samples):
            margin = y[i] * (sum(weights[j] * X[i][j] for j in range(n_features)) + bias)

            if margin >= 1:
                for j in range(n_features):
                    weights[j] -= lr * weights[j]
            else:
                for j in range(n_features):
                    weights[j] -= lr * (weights[j] - C * y[i] * X[i][j])
                bias += lr * C * y[i]

    return weights, bias


def predict(X, weights, bias):
    return [1 if sum(weights[j] * row[j] for j in range(len(weights))) + bias >= 0 else -1 for row in X]


if __name__ == "__main__":
    X = [[1, 1], [2, 1], [1, 2], [8, 8], [9, 8], [8, 9]]
    y = [-1, -1, -1, 1, 1, 1]

    weights, bias = train(X, y)
    print("Weights:", [round(w, 3) for w in weights], "Bias:", round(bias, 3))
    print("Predictions:", predict(X, weights, bias))

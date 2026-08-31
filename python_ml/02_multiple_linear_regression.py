"""ML Practice: Multiple Linear Regression using Gradient Descent"""


def train(X, y, lr=0.01, epochs=1000):
    n_samples = len(X)
    n_features = len(X[0])
    weights = [0.0] * n_features
    bias = 0.0

    for _ in range(epochs):
        y_pred = [sum(weights[j] * X[i][j] for j in range(n_features)) + bias for i in range(n_samples)]
        errors = [y_pred[i] - y[i] for i in range(n_samples)]

        for j in range(n_features):
            grad_w = (2 / n_samples) * sum(errors[i] * X[i][j] for i in range(n_samples))
            weights[j] -= lr * grad_w

        grad_b = (2 / n_samples) * sum(errors)
        bias -= lr * grad_b

    return weights, bias


def predict(X, weights, bias):
    return [sum(weights[j] * row[j] for j in range(len(weights))) + bias for row in X]


if __name__ == "__main__":
    X = [[1, 1], [2, 1], [3, 2], [4, 3], [5, 4]]
    y = [6, 8, 12, 16, 20]

    weights, bias = train(X, y, lr=0.02, epochs=2000)
    print("Weights:", [round(w, 3) for w in weights], "Bias:", round(bias, 3))
    print("Predictions:", [round(p, 2) for p in predict(X, weights, bias)])

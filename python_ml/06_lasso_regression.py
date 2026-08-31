"""ML Practice: Lasso Regression (L1 Regularization) using Gradient Descent"""


def sign(value):
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0


def train(X, y, lr=0.01, epochs=1000, alpha=0.1):
    n_samples = len(X)
    n_features = len(X[0])
    weights = [0.0] * n_features
    bias = 0.0

    for _ in range(epochs):
        y_pred = [sum(weights[j] * X[i][j] for j in range(n_features)) + bias for i in range(n_samples)]
        errors = [y_pred[i] - y[i] for i in range(n_samples)]

        for j in range(n_features):
            grad_w = (2 / n_samples) * sum(errors[i] * X[i][j] for i in range(n_samples))
            grad_w += alpha * sign(weights[j])
            weights[j] -= lr * grad_w

        grad_b = (2 / n_samples) * sum(errors)
        bias -= lr * grad_b

    return weights, bias


def predict(X, weights, bias):
    return [sum(weights[j] * row[j] for j in range(len(weights))) + bias for row in X]


if __name__ == "__main__":
    X = [[1], [2], [3], [4], [5]]
    y = [3, 5, 7, 9, 11]

    weights, bias = train(X, y, alpha=0.1)
    print("Weights:", [round(w, 3) for w in weights], "Bias:", round(bias, 3))
    print("Predictions:", [round(p, 2) for p in predict(X, weights, bias)])

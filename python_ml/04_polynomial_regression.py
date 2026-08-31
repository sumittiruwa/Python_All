"""ML Practice: Polynomial Regression using Gradient Descent"""


def make_polynomial_features(x, degree):
    return [[xi ** d for d in range(1, degree + 1)] for xi in x]


def train(X, y, lr=0.001, epochs=5000):
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
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]

    X = make_polynomial_features(x, degree=2)
    weights, bias = train(X, y)
    print("Weights:", [round(w, 3) for w in weights], "Bias:", round(bias, 3))
    print("Predictions:", [round(p, 2) for p in predict(X, weights, bias)])

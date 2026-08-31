"""ML Practice: Bias-Variance Tradeoff Demonstration (underfit vs overfit polynomial fit)"""


def fit_polynomial(x, y, degree, lr=0.0005, epochs=3000):
    n_features = degree
    weights = [0.0] * n_features
    bias = 0.0
    X = [[xi ** d for d in range(1, degree + 1)] for xi in x]

    for _ in range(epochs):
        y_pred = [sum(weights[j] * row[j] for j in range(n_features)) + bias for row in X]
        errors = [y_pred[i] - y[i] for i in range(len(x))]

        for j in range(n_features):
            grad = (2 / len(x)) * sum(errors[i] * X[i][j] for i in range(len(x)))
            weights[j] -= lr * grad
        bias -= lr * (2 / len(x)) * sum(errors)

    return weights, bias, X


def mse(y_true, y_pred):
    return sum((y_true[i] - y_pred[i]) ** 2 for i in range(len(y_true))) / len(y_true)


def predict(X, weights, bias):
    return [sum(weights[j] * row[j] for j in range(len(weights))) + bias for row in X]


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [2.1, 4.3, 6.2, 8.5, 10.1, 11.9, 14.2]

    for degree in [1, 3, 6]:
        weights, bias, X = fit_polynomial(x, y, degree)
        y_pred = predict(X, weights, bias)
        print(f"Degree {degree} -> Train MSE: {round(mse(y, y_pred), 4)}")

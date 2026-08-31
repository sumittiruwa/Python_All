"""ML Practice: Perceptron - the simplest neural network binary classifier"""


def activation(z):
    return 1 if z >= 0 else 0


def train(X, y, lr=0.1, epochs=20):
    n_features = len(X[0])
    weights = [0.0] * n_features
    bias = 0.0

    for _ in range(epochs):
        for i in range(len(X)):
            z = sum(weights[j] * X[i][j] for j in range(n_features)) + bias
            y_pred = activation(z)
            error = y[i] - y_pred

            for j in range(n_features):
                weights[j] += lr * error * X[i][j]
            bias += lr * error

    return weights, bias


def predict(X, weights, bias):
    return [activation(sum(weights[j] * row[j] for j in range(len(weights))) + bias) for row in X]


if __name__ == "__main__":
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y = [0, 0, 0, 1]  # AND gate

    weights, bias = train(X, y)
    print("Weights:", [round(w, 3) for w in weights], "Bias:", round(bias, 3))
    print("Predictions (AND gate):", predict(X, weights, bias))

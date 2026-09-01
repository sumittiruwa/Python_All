"""ML Practice: L1 vs L2 Regularization Effect on Weights"""


def train(X, y, lr=0.005, epochs=300, l1=0.0, l2=0.0):
    n_features = len(X[0])
    weights = [0.0] * n_features
    bias = 0.0
    n = len(X)

    for _ in range(epochs):
        grad_w = [0.0] * n_features
        grad_b = 0.0

        for xi, yi in zip(X, y):
            pred = sum(w * x for w, x in zip(weights, xi)) + bias
            error = pred - yi
            for j in range(n_features):
                grad_w[j] += error * xi[j]
            grad_b += error

        for j in range(n_features):
            l1_term = l1 * (1 if weights[j] > 0 else -1 if weights[j] < 0 else 0)
            weights[j] -= lr * (grad_w[j] / n + l1_term + l2 * weights[j])
        bias -= lr * (grad_b / n)

    return weights, bias


if __name__ == "__main__":
    X = [[1, 5, 0.1], [2, 4, 0.2], [3, 6, 0.1], [4, 5, 0.3], [5, 7, 0.2], [6, 6, 0.4]]
    y = [3, 5, 7, 9, 11, 13]

    w_none, b_none = train(X, y, l1=0.0, l2=0.0)
    w_l1, b_l1 = train(X, y, l1=0.3, l2=0.0)
    w_l2, b_l2 = train(X, y, l1=0.0, l2=0.3)

    print("No regularization:", [round(w, 3) for w in w_none])
    print("L1 regularization:", [round(w, 3) for w in w_l1])
    print("L2 regularization:", [round(w, 3) for w in w_l2])

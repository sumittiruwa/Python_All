"""ML Practice: Recursive Feature Elimination Wrapper"""


def train_linear_regression(X, y, lr=0.01, epochs=300):
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
        weights = [w - lr * (g / n) for w, g in zip(weights, grad_w)]
        bias -= lr * (grad_b / n)

    return weights, bias


def recursive_feature_elimination(X, y, n_features_to_keep):
    active = list(range(len(X[0])))

    while len(active) > n_features_to_keep:
        X_active = [[row[j] for j in active] for row in X]
        weights, _ = train_linear_regression(X_active, y)
        weakest_pos = min(range(len(weights)), key=lambda i: abs(weights[i]))
        removed_feature = active.pop(weakest_pos)
        print(f"Removing feature {removed_feature} (weight={weights[weakest_pos]:.4f})")

    return active


if __name__ == "__main__":
    X = [[1, 5, 10], [2, 4, 10.2], [3, 6, 9.8], [4, 3, 10.5], [5, 7, 9.7]]
    y = [2, 4, 6, 8, 10]

    kept = recursive_feature_elimination(X, y, n_features_to_keep=1)
    print("Final selected features:", kept)

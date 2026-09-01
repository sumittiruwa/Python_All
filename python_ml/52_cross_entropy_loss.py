"""ML Practice: Binary and Categorical Cross-Entropy Loss and Gradient"""

import math

EPS = 1e-12


def binary_cross_entropy(y_true, y_pred):
    losses = [-(y * math.log(p + EPS) + (1 - y) * math.log(1 - p + EPS)) for y, p in zip(y_true, y_pred)]
    return sum(losses) / len(losses)


def binary_cross_entropy_grad(y_true, y_pred):
    return [(p - y) / (p * (1 - p) + EPS) for y, p in zip(y_true, y_pred)]


def categorical_cross_entropy(y_true, y_pred):
    losses = []
    for true_vec, pred_vec in zip(y_true, y_pred):
        losses.append(-sum(t * math.log(p + EPS) for t, p in zip(true_vec, pred_vec)))
    return sum(losses) / len(losses)


if __name__ == "__main__":
    y_true = [1, 0, 1, 1]
    y_pred = [0.9, 0.2, 0.6, 0.4]

    print("Binary cross-entropy:", round(binary_cross_entropy(y_true, y_pred), 4))
    print("Gradient wrt predictions:", [round(g, 3) for g in binary_cross_entropy_grad(y_true, y_pred)])

    y_true_cat = [[1, 0, 0], [0, 1, 0]]
    y_pred_cat = [[0.7, 0.2, 0.1], [0.1, 0.8, 0.1]]
    print("Categorical cross-entropy:", round(categorical_cross_entropy(y_true_cat, y_pred_cat), 4))

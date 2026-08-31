"""ML Practice: Common Loss Functions used in ML training"""

import math


def mean_squared_error(y_true, y_pred):
    n = len(y_true)
    return sum((y_true[i] - y_pred[i]) ** 2 for i in range(n)) / n


def mean_absolute_error(y_true, y_pred):
    n = len(y_true)
    return sum(abs(y_true[i] - y_pred[i]) for i in range(n)) / n


def binary_cross_entropy(y_true, y_pred, epsilon=1e-12):
    n = len(y_true)
    total = 0.0
    for i in range(n):
        p = min(max(y_pred[i], epsilon), 1 - epsilon)
        total += -(y_true[i] * math.log(p) + (1 - y_true[i]) * math.log(1 - p))
    return total / n


def hinge_loss(y_true, y_pred):
    n = len(y_true)
    return sum(max(0, 1 - y_true[i] * y_pred[i]) for i in range(n)) / n


if __name__ == "__main__":
    y_true = [1, 0, 1, 1]
    y_pred_probs = [0.9, 0.1, 0.8, 0.6]

    print("MSE:", round(mean_squared_error([3, -0.5, 2, 7], [2.5, 0.0, 2, 8]), 4))
    print("MAE:", round(mean_absolute_error([3, -0.5, 2, 7], [2.5, 0.0, 2, 8]), 4))
    print("Binary Cross Entropy:", round(binary_cross_entropy(y_true, y_pred_probs), 4))
    print("Hinge Loss:", round(hinge_loss([1, -1, 1, -1], [0.8, -0.9, 0.3, 0.2]), 4))

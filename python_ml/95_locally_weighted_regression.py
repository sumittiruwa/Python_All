"""ML Practice: Locally Weighted (Kernel-Weighted) Linear Regression"""

import math


def gaussian_weight(x, xi, tau):
    return math.exp(-((x - xi) ** 2) / (2 * tau ** 2))


def locally_weighted_predict(x, X, y, tau=1.0):
    weights = [gaussian_weight(x, xi, tau) for xi in X]

    w_sum = sum(weights)
    w_x_sum = sum(w * xi for w, xi in zip(weights, X))
    w_y_sum = sum(w * yi for w, yi in zip(weights, y))
    w_xy_sum = sum(w * xi * yi for w, xi, yi in zip(weights, X, y))
    w_xx_sum = sum(w * xi ** 2 for w, xi in zip(weights, X))

    denom = w_sum * w_xx_sum - w_x_sum ** 2
    if abs(denom) < 1e-9:
        return w_y_sum / w_sum

    slope = (w_sum * w_xy_sum - w_x_sum * w_y_sum) / denom
    intercept = (w_y_sum - slope * w_x_sum) / w_sum
    return slope * x + intercept


if __name__ == "__main__":
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [1, 1.5, 4, 4.2, 4.8, 8, 8.5, 9, 12, 12.5]

    for query in [2.5, 5.5, 8.5]:
        pred = locally_weighted_predict(query, X, y, tau=1.5)
        print(f"x={query}: predicted y={pred:.3f}")

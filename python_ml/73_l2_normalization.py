"""ML Practice: L2 Vector Normalization of Feature Rows"""

import math


def l2_normalize(row):
    norm = math.sqrt(sum(v ** 2 for v in row))
    if norm == 0:
        return row[:]
    return [v / norm for v in row]


def l2_normalize_rows(X):
    return [l2_normalize(row) for row in X]


if __name__ == "__main__":
    X = [[3, 4], [1, 1, 1], [0, 5, 12], [0, 0, 0]]

    for row in X:
        normalized = l2_normalize(row)
        norm_check = math.sqrt(sum(v ** 2 for v in normalized))
        print(f"{row} -> {[round(v, 3) for v in normalized]} (norm={norm_check:.3f})")

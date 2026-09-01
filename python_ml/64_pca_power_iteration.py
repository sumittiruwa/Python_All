"""ML Practice: PCA Top Eigenvector via Power Iteration"""

import math


def mean_center(X):
    n_features = len(X[0])
    means = [sum(row[j] for row in X) / len(X) for j in range(n_features)]
    return [[row[j] - means[j] for j in range(n_features)] for row in X], means


def covariance_matrix(X):
    n_features = len(X[0])
    n = len(X)
    return [
        [sum(X[k][i] * X[k][j] for k in range(n)) / (n - 1) for j in range(n_features)]
        for i in range(n_features)
    ]


def matvec(matrix, vec):
    return [sum(row[j] * vec[j] for j in range(len(vec))) for row in matrix]


def normalize(vec):
    norm = math.sqrt(sum(v ** 2 for v in vec))
    return [v / norm for v in vec]


def power_iteration(matrix, iterations=100):
    vec = [1.0] * len(matrix)
    for _ in range(iterations):
        vec = normalize(matvec(matrix, vec))
    eigenvalue = sum(v * mv for v, mv in zip(vec, matvec(matrix, vec)))
    return vec, eigenvalue


if __name__ == "__main__":
    X = [[2.5, 2.4], [0.5, 0.7], [2.2, 2.9], [1.9, 2.2], [3.1, 3.0], [2.3, 2.7], [2.0, 1.6]]

    centered, means = mean_center(X)
    cov = covariance_matrix(centered)
    top_vec, top_val = power_iteration(cov)

    print("Covariance matrix:", [[round(v, 3) for v in row] for row in cov])
    print("Top eigenvector:", [round(v, 3) for v in top_vec])
    print("Top eigenvalue:", round(top_val, 3))

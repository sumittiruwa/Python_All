"""ML Practice: Principal Component Analysis (2D power-iteration based PCA)"""


def mean_center(X):
    n_features = len(X[0])
    means = [sum(row[j] for row in X) / len(X) for j in range(n_features)]
    centered = [[row[j] - means[j] for j in range(n_features)] for row in X]
    return centered, means


def covariance_matrix(X):
    n_features = len(X[0])
    n = len(X)
    cov = [[0.0] * n_features for _ in range(n_features)]
    for i in range(n_features):
        for j in range(n_features):
            cov[i][j] = sum(row[i] * row[j] for row in X) / (n - 1)
    return cov


def power_iteration(matrix, n_iter=100):
    n = len(matrix)
    vector = [1.0] * n

    for _ in range(n_iter):
        new_vector = [sum(matrix[i][j] * vector[j] for j in range(n)) for i in range(n)]
        norm = sum(v ** 2 for v in new_vector) ** 0.5
        vector = [v / norm for v in new_vector]

    eigenvalue = sum(vector[i] * sum(matrix[i][j] * vector[j] for j in range(n)) for i in range(n))
    return eigenvalue, vector


def pca_first_component(X):
    centered, _ = mean_center(X)
    cov = covariance_matrix(centered)
    eigenvalue, eigenvector = power_iteration(cov)
    projections = [sum(row[j] * eigenvector[j] for j in range(len(row))) for row in centered]
    return eigenvector, projections


if __name__ == "__main__":
    X = [[2.5, 2.4], [0.5, 0.7], [2.2, 2.9], [1.9, 2.2], [3.1, 3.0], [2.3, 2.7]]

    eigenvector, projections = pca_first_component(X)
    print("First principal component direction:", [round(v, 3) for v in eigenvector])
    print("Projections onto first component:", [round(p, 3) for p in projections])

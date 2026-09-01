"""ML Practice: Variance Threshold Feature Selection"""


def feature_variances(X):
    n_features = len(X[0])
    variances = []
    for j in range(n_features):
        col = [row[j] for row in X]
        mean = sum(col) / len(col)
        variances.append(sum((v - mean) ** 2 for v in col) / len(col))
    return variances


def select_by_variance(X, threshold=0.1):
    variances = feature_variances(X)
    keep = [j for j, v in enumerate(variances) if v > threshold]
    reduced = [[row[j] for j in keep] for row in X]
    return reduced, keep, variances


if __name__ == "__main__":
    X = [
        [1.0, 5, 100, 2.1],
        [1.0, 6, 102, 2.5],
        [1.0, 4, 98, 1.9],
        [1.0, 7, 105, 3.0],
    ]

    reduced, kept_indices, variances = select_by_variance(X, threshold=0.5)
    print("Feature variances:", [round(v, 3) for v in variances])
    print("Kept feature indices:", kept_indices)
    print("Reduced data:", reduced)

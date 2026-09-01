"""ML Practice: Polynomial Feature Expansion Utility"""

from itertools import combinations_with_replacement


def polynomial_features(X, degree=2):
    n_features = len(X[0])
    expanded = []

    for row in X:
        new_row = [1.0]
        for d in range(1, degree + 1):
            for combo in combinations_with_replacement(range(n_features), d):
                value = 1.0
                for idx in combo:
                    value *= row[idx]
                new_row.append(value)
        expanded.append(new_row)

    return expanded


if __name__ == "__main__":
    X = [[2, 3], [1, 4]]

    expanded = polynomial_features(X, degree=2)
    print("Original:", X)
    print("Expanded (degree 2, includes bias, x1, x2, x1^2, x1*x2, x2^2):")
    for row in expanded:
        print(" ", row)

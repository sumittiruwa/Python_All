"""ML Practice: K-Fold Cross Validation Split"""

import random


def k_fold_split(X, y, k=5, seed=42):
    random.seed(seed)
    n = len(X)
    indices = list(range(n))
    random.shuffle(indices)

    fold_size = n // k
    folds = [indices[i * fold_size: (i + 1) * fold_size] for i in range(k)]

    remainder = indices[k * fold_size:]
    for i, idx in enumerate(remainder):
        folds[i].append(idx)

    splits = []
    for i in range(k):
        test_idx = folds[i]
        train_idx = [idx for fold in folds if fold is not test_idx for idx in fold]
        X_train = [X[j] for j in train_idx]
        X_test = [X[j] for j in test_idx]
        y_train = [y[j] for j in train_idx]
        y_test = [y[j] for j in test_idx]
        splits.append((X_train, X_test, y_train, y_test))

    return splits


if __name__ == "__main__":
    X = [[i] for i in range(10)]
    y = list(range(10))

    splits = k_fold_split(X, y, k=5)
    for fold_idx, (X_train, X_test, y_train, y_test) in enumerate(splits):
        print(f"Fold {fold_idx}: train={y_train}, test={y_test}")

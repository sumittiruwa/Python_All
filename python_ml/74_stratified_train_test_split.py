"""ML Practice: Stratified Train/Test Split Preserving Class Ratios"""

import random
from collections import defaultdict


def stratified_split(X, y, test_ratio=0.3, seed=0):
    random.seed(seed)
    by_class = defaultdict(list)
    for xi, yi in zip(X, y):
        by_class[yi].append(xi)

    X_train, y_train, X_test, y_test = [], [], [], []

    for label, items in by_class.items():
        shuffled = items[:]
        random.shuffle(shuffled)
        n_test = round(len(shuffled) * test_ratio)
        test_items = shuffled[:n_test]
        train_items = shuffled[n_test:]

        X_test.extend(test_items)
        y_test.extend([label] * len(test_items))
        X_train.extend(train_items)
        y_train.extend([label] * len(train_items))

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    X = [[i] for i in range(20)]
    y = [0] * 15 + [1] * 5

    X_train, X_test, y_train, y_test = stratified_split(X, y, test_ratio=0.3)

    print("Train class distribution:", {c: y_train.count(c) for c in set(y_train)})
    print("Test class distribution: ", {c: y_test.count(c) for c in set(y_test)})
    print("Train size:", len(X_train), "Test size:", len(X_test))

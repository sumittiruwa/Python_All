"""ML Practice: Train-Test Split Utility"""

import random


def train_test_split(X, y, test_size=0.2, seed=42):
    random.seed(seed)
    n = len(X)
    indices = list(range(n))
    random.shuffle(indices)

    split_point = int(n * (1 - test_size))
    train_idx, test_idx = indices[:split_point], indices[split_point:]

    X_train = [X[i] for i in train_idx]
    X_test = [X[i] for i in test_idx]
    y_train = [y[i] for i in train_idx]
    y_test = [y[i] for i in test_idx]

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    X = [[i] for i in range(10)]
    y = list(range(10))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    print("Train size:", len(X_train), "Test size:", len(X_test))
    print("y_train:", y_train)
    print("y_test:", y_test)

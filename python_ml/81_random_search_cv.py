"""ML Practice: Random Search Hyperparameter Tuning"""

import random


def knn_predict(X_train, y_train, x, k):
    distances = sorted(
        range(len(X_train)),
        key=lambda i: sum((X_train[i][d] - x[d]) ** 2 for d in range(len(x))),
    )
    neighbors = [y_train[i] for i in distances[:k]]
    return max(set(neighbors), key=neighbors.count)


def cross_val_accuracy(X, y, k_neighbors, k_folds=3, seed=0):
    order = list(range(len(X)))
    random.seed(seed)
    random.shuffle(order)
    X, y = [X[i] for i in order], [y[i] for i in order]

    fold_size = len(X) // k_folds
    accuracies = []
    for i in range(k_folds):
        test_idx = set(range(i * fold_size, (i + 1) * fold_size))
        train_idx = [j for j in range(len(X)) if j not in test_idx]
        X_train, y_train = [X[j] for j in train_idx], [y[j] for j in train_idx]

        correct = sum(knn_predict(X_train, y_train, X[j], k_neighbors) == y[j] for j in test_idx)
        accuracies.append(correct / len(test_idx))

    return sum(accuracies) / len(accuracies)


def random_search(X, y, param_space, n_trials=5, seed=1):
    random.seed(seed)
    results = []
    for _ in range(n_trials):
        k_neighbors = random.choice(param_space["k_neighbors"])
        acc = cross_val_accuracy(X, y, k_neighbors)
        results.append((k_neighbors, acc))
    results.sort(key=lambda r: r[1], reverse=True)
    return results


if __name__ == "__main__":
    X = [[1, 1], [1.5, 1], [1, 1.5], [8, 8], [8.5, 8], [8, 8.5], [4, 4], [4.2, 4.1], [3.9, 4]]
    y = [0, 0, 0, 1, 1, 1, 2, 2, 2]

    results = random_search(X, y, {"k_neighbors": [1, 2, 3, 4, 5]}, n_trials=5)
    print("Random search trials (k_neighbors, cv_accuracy):")
    for k_neighbors, acc in results:
        print(f"  k={k_neighbors}: accuracy={acc:.3f}")
    print("Best k found:", results[0][0])

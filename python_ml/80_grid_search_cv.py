"""ML Practice: Grid Search Hyperparameter Tuning with Cross-Validation"""

import random


def knn_predict(X_train, y_train, x, k):
    distances = sorted(
        range(len(X_train)),
        key=lambda i: sum((X_train[i][d] - x[d]) ** 2 for d in range(len(x))),
    )
    neighbors = [y_train[i] for i in distances[:k]]
    return max(set(neighbors), key=neighbors.count)


def k_fold_indices(n, k_folds):
    fold_size = n // k_folds
    indices = list(range(n))
    folds = [indices[i * fold_size:(i + 1) * fold_size] for i in range(k_folds)]
    for i in range(n % k_folds):
        folds[i].append(indices[k_folds * fold_size + i])
    return folds


def cross_val_accuracy(X, y, k_neighbors, k_folds=3, seed=0):
    order = list(range(len(X)))
    random.seed(seed)
    random.shuffle(order)
    X, y = [X[i] for i in order], [y[i] for i in order]
    folds = k_fold_indices(len(X), k_folds)
    accuracies = []

    for i in range(k_folds):
        test_idx = set(folds[i])
        train_idx = [j for j in range(len(X)) if j not in test_idx]
        X_train, y_train = [X[j] for j in train_idx], [y[j] for j in train_idx]

        correct = 0
        for j in folds[i]:
            pred = knn_predict(X_train, y_train, X[j], k_neighbors)
            correct += pred == y[j]
        accuracies.append(correct / len(folds[i]))

    return sum(accuracies) / len(accuracies)


def grid_search(X, y, param_grid, k_folds=3):
    results = []
    for k_neighbors in param_grid["k_neighbors"]:
        acc = cross_val_accuracy(X, y, k_neighbors, k_folds)
        results.append((k_neighbors, acc))
    results.sort(key=lambda r: r[1], reverse=True)
    return results


if __name__ == "__main__":
    X = [[1, 1], [1.5, 1], [1, 1.5], [8, 8], [8.5, 8], [8, 8.5], [4, 4], [4.2, 4.1], [3.9, 4]]
    y = [0, 0, 0, 1, 1, 1, 2, 2, 2]

    results = grid_search(X, y, {"k_neighbors": [1, 2, 3, 4]}, k_folds=3)
    print("Grid search results (k_neighbors, cv_accuracy):")
    for k_neighbors, acc in results:
        print(f"  k={k_neighbors}: accuracy={acc:.3f}")
    print("Best k:", results[0][0])

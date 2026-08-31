"""ML Practice: Random Forest via Bagging of simple Decision Stumps"""

import random
from collections import Counter


def gini(labels):
    counts = Counter(labels)
    n = len(labels)
    return 1 - sum((count / n) ** 2 for count in counts.values())


def best_stump(X, y):
    best_gini, best_feature, best_threshold = float("inf"), None, None
    n_features = len(X[0])

    for feature in range(n_features):
        thresholds = set(row[feature] for row in X)
        for threshold in thresholds:
            left_y = [y[i] for i in range(len(X)) if X[i][feature] <= threshold]
            right_y = [y[i] for i in range(len(X)) if X[i][feature] > threshold]
            if not left_y or not right_y:
                continue
            weighted_gini = (len(left_y) * gini(left_y) + len(right_y) * gini(right_y)) / len(y)
            if weighted_gini < best_gini:
                best_gini, best_feature, best_threshold = weighted_gini, feature, threshold

    left_label = Counter(y[i] for i in range(len(X)) if X[i][best_feature] <= best_threshold).most_common(1)[0][0]
    right_label = Counter(y[i] for i in range(len(X)) if X[i][best_feature] > best_threshold).most_common(1)[0][0]

    return best_feature, best_threshold, left_label, right_label


def bootstrap_sample(X, y, seed):
    random.seed(seed)
    n = len(X)
    indices = [random.randint(0, n - 1) for _ in range(n)]
    return [X[i] for i in indices], [y[i] for i in indices]


def random_forest_train(X, y, n_trees=5):
    trees = []
    for seed in range(n_trees):
        X_sample, y_sample = bootstrap_sample(X, y, seed)
        trees.append(best_stump(X_sample, y_sample))
    return trees


def random_forest_predict(trees, row):
    votes = []
    for feature, threshold, left_label, right_label in trees:
        votes.append(left_label if row[feature] <= threshold else right_label)
    return Counter(votes).most_common(1)[0][0]


if __name__ == "__main__":
    X = [[2, 3], [1, 1], [8, 8], [9, 9], [1, 2], [8, 7]]
    y = ["A", "A", "B", "B", "A", "B"]

    forest = random_forest_train(X, y, n_trees=7)
    print("Prediction for [1.5, 1.5]:", random_forest_predict(forest, [1.5, 1.5]))
    print("Prediction for [8.5, 8.5]:", random_forest_predict(forest, [8.5, 8.5]))

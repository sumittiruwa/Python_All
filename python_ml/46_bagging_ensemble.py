"""ML Practice: Bootstrap Aggregating (Bagging) Ensemble of Decision Stumps"""

import random
from collections import Counter


def stump_predict(x, feature, threshold, polarity):
    return polarity if x[feature] < threshold else -polarity


def train_stump(X, y):
    best = {"error": float("inf")}
    for feature in range(len(X[0])):
        for threshold in sorted(set(x[feature] for x in X)):
            for polarity in (1, -1):
                error = sum(1 for x, label in zip(X, y) if stump_predict(x, feature, threshold, polarity) != label)
                if error < best["error"]:
                    best = {"feature": feature, "threshold": threshold, "polarity": polarity, "error": error}
    return best


def bootstrap_sample(X, y, seed):
    random.seed(seed)
    n = len(X)
    indices = [random.randrange(n) for _ in range(n)]
    return [X[i] for i in indices], [y[i] for i in indices]


def train_bagging(X, y, n_estimators=7):
    stumps = []
    for i in range(n_estimators):
        Xb, yb = bootstrap_sample(X, y, seed=i)
        stumps.append(train_stump(Xb, yb))
    return stumps


def predict(x, stumps):
    votes = [stump_predict(x, s["feature"], s["threshold"], s["polarity"]) for s in stumps]
    return Counter(votes).most_common(1)[0][0]


if __name__ == "__main__":
    X = [[1, 5], [2, 6], [3, 4], [2, 5], [6, 2], [7, 1], [8, 3], [7, 2]]
    y = [1, 1, 1, 1, -1, -1, -1, -1]

    stumps = train_bagging(X, y, n_estimators=9)

    for x in [[2, 4], [7, 3], [4, 4]]:
        print(f"{x} -> ensemble prediction {predict(x, stumps)}")

"""ML Practice: Decision Stump (Single-Split Weak Learner)"""


def stump_predict(x, feature, threshold, polarity):
    return polarity if x[feature] < threshold else -polarity


def best_stump(X, y, weights=None):
    n_samples = len(X)
    n_features = len(X[0])
    weights = weights or [1 / n_samples] * n_samples

    best = {"error": float("inf")}

    for feature in range(n_features):
        thresholds = sorted(set(x[feature] for x in X))
        for threshold in thresholds:
            for polarity in (1, -1):
                error = sum(
                    w for x, label, w in zip(X, y, weights)
                    if stump_predict(x, feature, threshold, polarity) != label
                )
                if error < best["error"]:
                    best = {
                        "feature": feature,
                        "threshold": threshold,
                        "polarity": polarity,
                        "error": error,
                    }

    return best


if __name__ == "__main__":
    X = [[1, 5], [2, 6], [3, 4], [6, 2], [7, 1], [8, 3]]
    y = [1, 1, 1, -1, -1, -1]

    stump = best_stump(X, y)
    print("Best stump:", stump)

    for x in X:
        pred = stump_predict(x, stump["feature"], stump["threshold"], stump["polarity"])
        print(f"{x} -> predicted {pred}")

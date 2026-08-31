"""ML Practice: AdaBoost using Decision Stumps (labels must be -1 or 1)"""

import math


def build_stump(X, y, weights):
    n_samples, n_features = len(X), len(X[0])
    best_stump = None
    min_error = float("inf")

    for feature in range(n_features):
        thresholds = set(row[feature] for row in X)
        for threshold in thresholds:
            for polarity in [1, -1]:
                predictions = []
                for row in X:
                    pred = 1 if polarity * row[feature] < polarity * threshold else -1
                    predictions.append(pred)

                error = sum(weights[i] for i in range(n_samples) if predictions[i] != y[i])

                if error < min_error:
                    min_error = error
                    best_stump = (feature, threshold, polarity, predictions)

    return best_stump, min_error


def adaboost_train(X, y, n_estimators=5):
    n_samples = len(X)
    weights = [1 / n_samples] * n_samples
    stumps = []

    for _ in range(n_estimators):
        (feature, threshold, polarity, predictions), error = build_stump(X, y, weights)
        error = max(error, 1e-10)
        alpha = 0.5 * math.log((1 - error) / error)

        weights = [weights[i] * math.exp(-alpha * y[i] * predictions[i]) for i in range(n_samples)]
        total = sum(weights)
        weights = [w / total for w in weights]

        stumps.append((feature, threshold, polarity, alpha))

    return stumps


def adaboost_predict(stumps, row):
    total = 0
    for feature, threshold, polarity, alpha in stumps:
        pred = 1 if polarity * row[feature] < polarity * threshold else -1
        total += alpha * pred
    return 1 if total > 0 else -1


if __name__ == "__main__":
    X = [[1], [2], [3], [8], [9], [10]]
    y = [-1, -1, -1, 1, 1, 1]

    stumps = adaboost_train(X, y, n_estimators=5)
    print("Prediction for [2.5]:", adaboost_predict(stumps, [2.5]))
    print("Prediction for [9.5]:", adaboost_predict(stumps, [9.5]))

"""ML Practice: Gaussian Naive Bayes Classifier"""

import math
from collections import defaultdict


def mean(values):
    return sum(values) / len(values)


def stdev(values):
    avg = mean(values)
    variance = sum((x - avg) ** 2 for x in values) / (len(values) - 1) if len(values) > 1 else 1e-9
    return math.sqrt(variance) or 1e-9


def summarize_by_class(X, y):
    class_data = defaultdict(list)
    for features, label in zip(X, y):
        class_data[label].append(features)

    summaries = {}
    for label, rows in class_data.items():
        n_features = len(rows[0])
        summaries[label] = [(mean([row[i] for row in rows]), stdev([row[i] for row in rows])) for i in range(n_features)]

    return summaries


def gaussian_probability(x, mean_val, stdev_val):
    exponent = math.exp(-((x - mean_val) ** 2) / (2 * stdev_val ** 2))
    return (1 / (math.sqrt(2 * math.pi) * stdev_val)) * exponent


def predict(summaries, row):
    best_label, best_prob = None, -1
    for label, feature_stats in summaries.items():
        prob = 1.0
        for i, (mean_val, stdev_val) in enumerate(feature_stats):
            prob *= gaussian_probability(row[i], mean_val, stdev_val)
        if prob > best_prob:
            best_prob = prob
            best_label = label
    return best_label


if __name__ == "__main__":
    X = [[1, 2], [1.5, 1.8], [5, 8], [6, 9], [1.2, 1.5], [5.5, 8.5]]
    y = ["A", "A", "B", "B", "A", "B"]

    summaries = summarize_by_class(X, y)
    print("Prediction for [1.3, 1.7]:", predict(summaries, [1.3, 1.7]))
    print("Prediction for [5.8, 8.2]:", predict(summaries, [5.8, 8.2]))

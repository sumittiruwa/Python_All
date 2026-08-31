"""ML Practice: K-Nearest Neighbors Classifier"""

import math
from collections import Counter


def euclidean_distance(a, b):
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))


def knn_predict(X_train, y_train, x_query, k=3):
    distances = [(euclidean_distance(x_query, X_train[i]), y_train[i]) for i in range(len(X_train))]
    distances.sort(key=lambda pair: pair[0])
    k_nearest_labels = [label for _, label in distances[:k]]
    return Counter(k_nearest_labels).most_common(1)[0][0]


if __name__ == "__main__":
    X_train = [[1, 1], [2, 1], [1, 2], [8, 8], [9, 8], [8, 9]]
    y_train = ["A", "A", "A", "B", "B", "B"]

    query = [2, 2]
    print(f"Prediction for {query}:", knn_predict(X_train, y_train, query, k=3))

    query = [8, 7]
    print(f"Prediction for {query}:", knn_predict(X_train, y_train, query, k=3))

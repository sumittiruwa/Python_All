"""ML Practice: K-Nearest Neighbors Regressor"""

import math


def euclidean_distance(a, b):
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))


def knn_predict(X_train, y_train, x_query, k=3):
    distances = [(euclidean_distance(x_query, X_train[i]), y_train[i]) for i in range(len(X_train))]
    distances.sort(key=lambda pair: pair[0])
    k_nearest_values = [value for _, value in distances[:k]]
    return sum(k_nearest_values) / len(k_nearest_values)


if __name__ == "__main__":
    X_train = [[1], [2], [3], [4], [5]]
    y_train = [1.5, 3.0, 4.5, 6.0, 7.5]

    query = [3.5]
    print(f"Prediction for {query}:", round(knn_predict(X_train, y_train, query, k=3), 3))

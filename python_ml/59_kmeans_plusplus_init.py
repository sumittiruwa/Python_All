"""ML Practice: K-Means++ Centroid Initialization"""

import math
import random


def euclidean_distance(a, b):
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))


def kmeans_plusplus_init(X, k, seed=42):
    random.seed(seed)
    centroids = [random.choice(X)]

    while len(centroids) < k:
        distances = [min(euclidean_distance(x, c) ** 2 for c in centroids) for x in X]
        total = sum(distances)
        probs = [d / total for d in distances]

        r = random.random()
        cumulative = 0.0
        for x, p in zip(X, probs):
            cumulative += p
            if r <= cumulative:
                centroids.append(x)
                break

    return centroids


if __name__ == "__main__":
    X = [[1, 1], [1.5, 2], [1, 0.5], [8, 8], [9, 9], [8.5, 8], [15, 1], [15.5, 1.5], [14.5, 0.5]]

    centroids = kmeans_plusplus_init(X, k=3)
    print("K-Means++ initial centroids:")
    for c in centroids:
        print(" ", c)

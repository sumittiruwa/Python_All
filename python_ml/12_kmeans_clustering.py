"""ML Practice: K-Means Clustering"""

import math
import random


def euclidean_distance(a, b):
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))


def kmeans(X, k, epochs=100, seed=42):
    random.seed(seed)
    centroids = random.sample(X, k)

    for _ in range(epochs):
        clusters = [[] for _ in range(k)]

        for point in X:
            distances = [euclidean_distance(point, c) for c in centroids]
            cluster_idx = distances.index(min(distances))
            clusters[cluster_idx].append(point)

        new_centroids = []
        for i, cluster in enumerate(clusters):
            if cluster:
                dims = len(cluster[0])
                centroid = [sum(p[d] for p in cluster) / len(cluster) for d in range(dims)]
                new_centroids.append(centroid)
            else:
                new_centroids.append(centroids[i])

        if new_centroids == centroids:
            break
        centroids = new_centroids

    labels = []
    for point in X:
        distances = [euclidean_distance(point, c) for c in centroids]
        labels.append(distances.index(min(distances)))

    return centroids, labels


if __name__ == "__main__":
    X = [[1, 1], [1.5, 2], [1, 0.5], [8, 8], [9, 9], [8.5, 8]]
    centroids, labels = kmeans(X, k=2)

    print("Centroids:", [[round(c, 2) for c in centroid] for centroid in centroids])
    print("Labels:", labels)

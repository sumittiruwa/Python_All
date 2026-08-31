"""ML Practice: Elbow Method to choose optimal k for K-Means Clustering"""

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
            clusters[distances.index(min(distances))].append(point)

        new_centroids = []
        for i, cluster in enumerate(clusters):
            if cluster:
                dims = len(cluster[0])
                new_centroids.append([sum(p[d] for p in cluster) / len(cluster) for d in range(dims)])
            else:
                new_centroids.append(centroids[i])

        if new_centroids == centroids:
            break
        centroids = new_centroids

    return centroids, clusters


def inertia(centroids, clusters):
    total = 0.0
    for centroid, cluster in zip(centroids, clusters):
        total += sum(euclidean_distance(point, centroid) ** 2 for point in cluster)
    return total


def elbow_method(X, max_k=6):
    results = []
    for k in range(1, max_k + 1):
        centroids, clusters = kmeans(X, k)
        results.append((k, round(inertia(centroids, clusters), 3)))
    return results


if __name__ == "__main__":
    X = [[1, 1], [1.5, 2], [1, 0.5], [8, 8], [9, 9], [8.5, 8], [15, 1], [15.5, 1.5], [14.5, 0.5]]

    for k, score in elbow_method(X, max_k=5):
        print(f"k={k}: inertia={score}")

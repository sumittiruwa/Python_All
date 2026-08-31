"""ML Practice: Agglomerative Hierarchical Clustering (single-linkage)"""

import math


def euclidean_distance(a, b):
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))


def cluster_distance(cluster_a, cluster_b, points):
    return min(euclidean_distance(points[i], points[j]) for i in cluster_a for j in cluster_b)


def agglomerative_clustering(points, n_clusters):
    clusters = [[i] for i in range(len(points))]

    while len(clusters) > n_clusters:
        best_pair = None
        best_distance = float("inf")

        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                dist = cluster_distance(clusters[i], clusters[j], points)
                if dist < best_distance:
                    best_distance = dist
                    best_pair = (i, j)

        i, j = best_pair
        merged = clusters[i] + clusters[j]
        clusters = [c for idx, c in enumerate(clusters) if idx not in (i, j)]
        clusters.append(merged)

    return clusters


if __name__ == "__main__":
    points = [[1, 1], [1.5, 2], [1, 0.5], [8, 8], [9, 9], [8.5, 8]]
    clusters = agglomerative_clustering(points, n_clusters=2)

    for idx, cluster in enumerate(clusters):
        print(f"Cluster {idx}:", [points[i] for i in cluster])

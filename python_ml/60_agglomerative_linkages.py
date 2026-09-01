"""ML Practice: Agglomerative Clustering with Single/Complete/Average Linkage"""

import math


def euclidean_distance(a, b):
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))


def cluster_distance(c1, c2, points, method):
    dists = [euclidean_distance(points[i], points[j]) for i in c1 for j in c2]
    if method == "single":
        return min(dists)
    if method == "complete":
        return max(dists)
    return sum(dists) / len(dists)


def agglomerative_clustering(points, n_clusters, method="single"):
    clusters = [[i] for i in range(len(points))]

    while len(clusters) > n_clusters:
        best_pair, best_dist = None, float("inf")
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                d = cluster_distance(clusters[i], clusters[j], points, method)
                if d < best_dist:
                    best_dist, best_pair = d, (i, j)

        i, j = best_pair
        merged = clusters[i] + clusters[j]
        clusters = [c for idx, c in enumerate(clusters) if idx not in (i, j)] + [merged]

    return clusters


if __name__ == "__main__":
    points = [[1, 1], [1.2, 1.1], [0.8, 0.9], [8, 8], [8.2, 7.8], [15, 1], [15.3, 1.2]]

    for method in ("single", "complete", "average"):
        clusters = agglomerative_clustering(points, n_clusters=3, method=method)
        print(f"{method} linkage:", clusters)

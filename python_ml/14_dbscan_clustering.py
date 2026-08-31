"""ML Practice: DBSCAN Clustering (density-based)"""

import math


def euclidean_distance(a, b):
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))


def region_query(points, point_idx, eps):
    return [i for i, p in enumerate(points) if euclidean_distance(points[point_idx], p) <= eps]


def dbscan(points, eps=1.5, min_pts=2):
    labels = [None] * len(points)
    cluster_id = 0

    for i in range(len(points)):
        if labels[i] is not None:
            continue

        neighbors = region_query(points, i, eps)
        if len(neighbors) < min_pts:
            labels[i] = -1  # noise
            continue

        labels[i] = cluster_id
        seeds = neighbors[:]
        j = 0
        while j < len(seeds):
            neighbor_idx = seeds[j]
            if labels[neighbor_idx] == -1:
                labels[neighbor_idx] = cluster_id
            if labels[neighbor_idx] is None:
                labels[neighbor_idx] = cluster_id
                neighbor_neighbors = region_query(points, neighbor_idx, eps)
                if len(neighbor_neighbors) >= min_pts:
                    seeds.extend(neighbor_neighbors)
            j += 1

        cluster_id += 1

    return labels


if __name__ == "__main__":
    points = [[1, 1], [1.2, 1.1], [0.9, 1], [8, 8], [8.1, 8.2], [25, 25]]
    labels = dbscan(points, eps=1.0, min_pts=2)
    print("Cluster labels (-1 = noise):", labels)

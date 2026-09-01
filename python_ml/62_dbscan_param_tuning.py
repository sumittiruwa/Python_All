"""ML Practice: DBSCAN eps/minPts Sensitivity Demo"""

import math


def euclidean_distance(a, b):
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))


def region_query(points, idx, eps):
    return [j for j in range(len(points)) if euclidean_distance(points[idx], points[j]) <= eps]


def dbscan(points, eps, min_pts):
    labels = [None] * len(points)
    cluster_id = 0

    for i in range(len(points)):
        if labels[i] is not None:
            continue

        neighbors = region_query(points, i, eps)
        if len(neighbors) < min_pts:
            labels[i] = -1
            continue

        labels[i] = cluster_id
        seeds = list(neighbors)
        while seeds:
            j = seeds.pop()
            if labels[j] == -1:
                labels[j] = cluster_id
            if labels[j] is not None:
                continue
            labels[j] = cluster_id
            j_neighbors = region_query(points, j, eps)
            if len(j_neighbors) >= min_pts:
                seeds.extend(j_neighbors)

        cluster_id += 1

    return labels


if __name__ == "__main__":
    points = [[1, 1], [1.1, 1.2], [0.9, 0.8], [8, 8], [8.2, 7.9], [15, 1], [1.5, 15]]

    for eps, min_pts in [(0.5, 2), (1.0, 2), (2.0, 3)]:
        labels = dbscan(points, eps, min_pts)
        n_clusters = len(set(labels) - {-1})
        n_noise = labels.count(-1)
        print(f"eps={eps}, min_pts={min_pts} -> labels={labels}, clusters={n_clusters}, noise={n_noise}")

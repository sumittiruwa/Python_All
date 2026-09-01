"""ML Practice: Silhouette Score for Clustering Quality"""

import math


def euclidean_distance(a, b):
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))


def silhouette_sample(idx, points, labels):
    own_label = labels[idx]
    same_cluster = [j for j in range(len(points)) if labels[j] == own_label and j != idx]

    if not same_cluster:
        return 0.0

    a = sum(euclidean_distance(points[idx], points[j]) for j in same_cluster) / len(same_cluster)

    other_labels = set(labels) - {own_label}
    b = min(
        sum(euclidean_distance(points[idx], points[j]) for j in range(len(points)) if labels[j] == label)
        / labels.count(label)
        for label in other_labels
    )

    return (b - a) / max(a, b)


def silhouette_score(points, labels):
    scores = [silhouette_sample(i, points, labels) for i in range(len(points))]
    return sum(scores) / len(scores)


if __name__ == "__main__":
    points = [[1, 1], [1.2, 1.1], [0.8, 0.9], [8, 8], [8.2, 7.8], [7.9, 8.1]]
    labels = [0, 0, 0, 1, 1, 1]

    for i, p in enumerate(points):
        print(f"{p}: silhouette={silhouette_sample(i, points, labels):.3f}")

    print("Average silhouette score:", round(silhouette_score(points, labels), 3))

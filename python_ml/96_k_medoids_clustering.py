"""ML Practice: K-Medoids (PAM-style) Clustering"""

import math


def euclidean_distance(a, b):
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))


def total_cost(points, medoid_indices):
    medoids = [points[i] for i in medoid_indices]
    return sum(min(euclidean_distance(p, m) for m in medoids) for p in points)


def assign_clusters(points, medoid_indices):
    medoids = [points[i] for i in medoid_indices]
    clusters = [[] for _ in medoid_indices]
    for idx, p in enumerate(points):
        distances = [euclidean_distance(p, m) for m in medoids]
        clusters[distances.index(min(distances))].append(idx)
    return clusters


def k_medoids(points, k, seed_indices=None):
    medoid_indices = seed_indices or list(range(k))
    improved = True

    while improved:
        improved = False
        best_cost = total_cost(points, medoid_indices)

        for m_pos in range(len(medoid_indices)):
            for candidate in range(len(points)):
                if candidate in medoid_indices:
                    continue
                trial = medoid_indices[:]
                trial[m_pos] = candidate
                cost = total_cost(points, trial)
                if cost < best_cost:
                    best_cost = cost
                    medoid_indices = trial
                    improved = True

    clusters = assign_clusters(points, medoid_indices)
    return medoid_indices, clusters


if __name__ == "__main__":
    points = [[1, 1], [1.5, 2], [1, 0.5], [8, 8], [9, 9], [8.5, 8], [15, 1], [15.5, 1.5]]

    medoid_indices, clusters = k_medoids(points, k=3, seed_indices=[0, 3, 6])

    print("Final medoids:", [points[i] for i in medoid_indices])
    for i, cluster in enumerate(clusters):
        print(f"Cluster {i}:", [points[j] for j in cluster])

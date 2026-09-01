"""ML Practice: Simplified Isolation-Forest-Style Anomaly Detection"""

import random
import math


class Node:
    def __init__(self, feature=None, split=None, left=None, right=None, size=0):
        self.feature = feature
        self.split = split
        self.left = left
        self.right = right
        self.size = size


def build_tree(points, depth, max_depth, rng):
    if depth >= max_depth or len(points) <= 1:
        return Node(size=len(points))

    feature = rng.randrange(len(points[0]))
    values = [p[feature] for p in points]
    if min(values) == max(values):
        return Node(size=len(points))

    split = rng.uniform(min(values), max(values))
    left_points = [p for p in points if p[feature] < split]
    right_points = [p for p in points if p[feature] >= split]

    return Node(
        feature=feature,
        split=split,
        left=build_tree(left_points, depth + 1, max_depth, rng),
        right=build_tree(right_points, depth + 1, max_depth, rng),
        size=len(points),
    )


def path_length(point, node, depth=0):
    if node.left is None or node.right is None:
        return depth + (math.log(max(node.size, 1) + 1) if node.size > 1 else 0)
    if point[node.feature] < node.split:
        return path_length(point, node.left, depth + 1)
    return path_length(point, node.right, depth + 1)


def isolation_forest(points, n_trees=50, max_depth=8, seed=1):
    rng = random.Random(seed)
    trees = [build_tree(points, 0, max_depth, rng) for _ in range(n_trees)]
    return trees


def anomaly_score(point, trees):
    avg_path = sum(path_length(point, tree) for tree in trees) / len(trees)
    return 2 ** (-avg_path / 3)


if __name__ == "__main__":
    points = [[1, 1], [1.2, 1.1], [0.9, 0.8], [1.1, 1.0], [1.0, 0.9], [10, 10]]

    trees = isolation_forest(points)
    for p in points:
        score = anomaly_score(p, trees)
        print(f"{p} -> anomaly score={score:.3f}")

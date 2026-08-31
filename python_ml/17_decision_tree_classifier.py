"""ML Practice: Decision Tree Classifier (Gini impurity, from scratch)"""

from collections import Counter


class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, label=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.label = label


def gini(labels):
    counts = Counter(labels)
    n = len(labels)
    return 1 - sum((count / n) ** 2 for count in counts.values())


def split(X, y, feature, threshold):
    left_X, left_y, right_X, right_y = [], [], [], []
    for row, label in zip(X, y):
        if row[feature] <= threshold:
            left_X.append(row)
            left_y.append(label)
        else:
            right_X.append(row)
            right_y.append(label)
    return left_X, left_y, right_X, right_y


def best_split(X, y):
    best_gini, best_feature, best_threshold = float("inf"), None, None
    n_features = len(X[0])

    for feature in range(n_features):
        thresholds = set(row[feature] for row in X)
        for threshold in thresholds:
            left_X, left_y, right_X, right_y = split(X, y, feature, threshold)
            if not left_y or not right_y:
                continue
            weighted_gini = (len(left_y) * gini(left_y) + len(right_y) * gini(right_y)) / len(y)
            if weighted_gini < best_gini:
                best_gini, best_feature, best_threshold = weighted_gini, feature, threshold

    return best_feature, best_threshold


def build_tree(X, y, depth=0, max_depth=5):
    if len(set(y)) == 1 or depth >= max_depth or len(y) < 2:
        return Node(label=Counter(y).most_common(1)[0][0])

    feature, threshold = best_split(X, y)
    if feature is None:
        return Node(label=Counter(y).most_common(1)[0][0])

    left_X, left_y, right_X, right_y = split(X, y, feature, threshold)
    left_node = build_tree(left_X, left_y, depth + 1, max_depth)
    right_node = build_tree(right_X, right_y, depth + 1, max_depth)

    return Node(feature=feature, threshold=threshold, left=left_node, right=right_node)


def predict_one(node, row):
    if node.label is not None:
        return node.label
    if row[node.feature] <= node.threshold:
        return predict_one(node.left, row)
    return predict_one(node.right, row)


if __name__ == "__main__":
    X = [[2, 3], [1, 1], [8, 8], [9, 9], [1, 2], [8, 7]]
    y = ["A", "A", "B", "B", "A", "B"]

    tree = build_tree(X, y)
    print("Prediction for [1.5, 1.5]:", predict_one(tree, [1.5, 1.5]))
    print("Prediction for [8.5, 8.5]:", predict_one(tree, [8.5, 8.5]))

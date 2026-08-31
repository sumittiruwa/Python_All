"""ML Practice: Decision Tree Regressor (variance reduction, from scratch)"""


class Node:
    def __init__(self, feature=None, threshold=None, left=None, right=None, value=None):
        self.feature = feature
        self.threshold = threshold
        self.left = left
        self.right = right
        self.value = value


def variance(values):
    if not values:
        return 0
    avg = sum(values) / len(values)
    return sum((v - avg) ** 2 for v in values) / len(values)


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
    best_score, best_feature, best_threshold = float("inf"), None, None
    n_features = len(X[0])

    for feature in range(n_features):
        thresholds = set(row[feature] for row in X)
        for threshold in thresholds:
            left_X, left_y, right_X, right_y = split(X, y, feature, threshold)
            if not left_y or not right_y:
                continue
            score = (len(left_y) * variance(left_y) + len(right_y) * variance(right_y)) / len(y)
            if score < best_score:
                best_score, best_feature, best_threshold = score, feature, threshold

    return best_feature, best_threshold


def build_tree(X, y, depth=0, max_depth=4):
    if depth >= max_depth or len(y) < 2 or variance(y) == 0:
        return Node(value=sum(y) / len(y))

    feature, threshold = best_split(X, y)
    if feature is None:
        return Node(value=sum(y) / len(y))

    left_X, left_y, right_X, right_y = split(X, y, feature, threshold)
    left_node = build_tree(left_X, left_y, depth + 1, max_depth)
    right_node = build_tree(right_X, right_y, depth + 1, max_depth)

    return Node(feature=feature, threshold=threshold, left=left_node, right=right_node)


def predict_one(node, row):
    if node.value is not None:
        return node.value
    if row[node.feature] <= node.threshold:
        return predict_one(node.left, row)
    return predict_one(node.right, row)


if __name__ == "__main__":
    X = [[1], [2], [3], [8], [9], [10]]
    y = [1.1, 1.9, 3.2, 8.1, 9.0, 10.2]

    tree = build_tree(X, y)
    print("Prediction for [2.5]:", round(predict_one(tree, [2.5]), 2))
    print("Prediction for [9.5]:", round(predict_one(tree, [9.5]), 2))

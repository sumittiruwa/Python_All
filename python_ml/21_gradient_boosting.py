"""ML Practice: Gradient Boosting for Regression (using simple stumps)"""


def build_stump(X, y):
    n_features = len(X[0])
    best_feature, best_threshold, best_score = None, None, float("inf")
    best_left_val, best_right_val = None, None

    for feature in range(n_features):
        thresholds = set(row[feature] for row in X)
        for threshold in thresholds:
            left = [y[i] for i in range(len(X)) if X[i][feature] <= threshold]
            right = [y[i] for i in range(len(X)) if X[i][feature] > threshold]
            if not left or not right:
                continue

            left_val = sum(left) / len(left)
            right_val = sum(right) / len(right)
            score = sum((v - left_val) ** 2 for v in left) + sum((v - right_val) ** 2 for v in right)

            if score < best_score:
                best_score = score
                best_feature, best_threshold = feature, threshold
                best_left_val, best_right_val = left_val, right_val

    return best_feature, best_threshold, best_left_val, best_right_val


def stump_predict(stump, row):
    feature, threshold, left_val, right_val = stump
    return left_val if row[feature] <= threshold else right_val


def gradient_boosting_train(X, y, n_estimators=10, lr=0.1):
    predictions = [sum(y) / len(y)] * len(y)
    initial_pred = predictions[0]
    stumps = []

    for _ in range(n_estimators):
        residuals = [y[i] - predictions[i] for i in range(len(y))]
        stump = build_stump(X, residuals)
        stumps.append(stump)
        predictions = [predictions[i] + lr * stump_predict(stump, X[i]) for i in range(len(X))]

    return initial_pred, stumps, lr


def gradient_boosting_predict(model, row):
    initial_pred, stumps, lr = model
    prediction = initial_pred
    for stump in stumps:
        prediction += lr * stump_predict(stump, row)
    return prediction


if __name__ == "__main__":
    X = [[1], [2], [3], [8], [9], [10]]
    y = [1.1, 1.9, 3.2, 8.1, 9.0, 10.2]

    model = gradient_boosting_train(X, y, n_estimators=20, lr=0.2)
    print("Prediction for [2.5]:", round(gradient_boosting_predict(model, [2.5]), 2))
    print("Prediction for [9.5]:", round(gradient_boosting_predict(model, [9.5]), 2))

"""ML Practice: Stacking Ensemble with a Meta-Learner"""


def base_mean_threshold(X, y):
    threshold = sum(sum(x) for x in X) / len(X)
    return lambda x: 1 if sum(x) >= threshold else 0


def base_nearest_centroid(X, y):
    class0 = [x for x, label in zip(X, y) if label == 0]
    class1 = [x for x, label in zip(X, y) if label == 1]
    c0 = [sum(v) / len(class0) for v in zip(*class0)]
    c1 = [sum(v) / len(class1) for v in zip(*class1)]

    def predict(x):
        d0 = sum((a - b) ** 2 for a, b in zip(x, c0))
        d1 = sum((a - b) ** 2 for a, b in zip(x, c1))
        return 1 if d1 < d0 else 0

    return predict


def train_meta_learner(meta_X, y, lr=0.3, epochs=300):
    weights = [0.0] * len(meta_X[0])
    bias = 0.0
    for _ in range(epochs):
        for xi, yi in zip(meta_X, y):
            pred = 1 / (1 + pow(2.718281828, -(sum(w * x for w, x in zip(weights, xi)) + bias)))
            error = yi - pred
            weights = [w + lr * error * x for w, x in zip(weights, xi)]
            bias += lr * error
    return weights, bias


def stacking_predict(x, base_models, weights, bias):
    meta_features = [model(x) for model in base_models]
    score = sum(w * f for w, f in zip(weights, meta_features)) + bias
    return 1 if score >= 0 else 0


if __name__ == "__main__":
    X = [[1, 1], [2, 1], [1, 2], [8, 8], [9, 8], [8, 9], [5, 5], [4, 6]]
    y = [0, 0, 0, 1, 1, 1, 1, 1]

    base_models = [base_mean_threshold(X, y), base_nearest_centroid(X, y)]
    meta_X = [[m(x) for m in base_models] for x in X]
    weights, bias = train_meta_learner(meta_X, y)

    for x in [[1.5, 1.5], [8.5, 8.5], [5, 4]]:
        print(f"{x} -> stacked prediction {stacking_predict(x, base_models, weights, bias)}")

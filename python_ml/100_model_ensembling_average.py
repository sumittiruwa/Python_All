"""ML Practice: Simple Ensembling by Averaging Multiple Models' Predictions"""


def model_a(x):
    return 2 * x[0] + 1


def model_b(x):
    return 1.8 * x[0] + 1.5


def model_c(x):
    return 2.2 * x[0] + 0.5


def average_ensemble(x, models, weights=None):
    weights = weights or [1] * len(models)
    total_weight = sum(weights)
    predictions = [m(x) for m in models]
    weighted_sum = sum(w * p for w, p in zip(weights, predictions))
    return predictions, weighted_sum / total_weight


if __name__ == "__main__":
    models = [model_a, model_b, model_c]
    samples = [[1], [3], [5]]

    for x in samples:
        predictions, ensembled = average_ensemble(x, models)
        weighted_predictions, weighted_ensembled = average_ensemble(x, models, weights=[2, 1, 1])
        print(f"x={x}: individual={[round(p, 2) for p in predictions]}, "
              f"simple_avg={ensembled:.3f}, weighted_avg={weighted_ensembled:.3f}")

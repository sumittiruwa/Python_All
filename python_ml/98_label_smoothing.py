"""ML Practice: Label Smoothing Regularization for Classification Targets"""

import math


def smooth_labels(one_hot, alpha=0.1):
    n_classes = len(one_hot)
    return [
        v * (1 - alpha) + alpha / n_classes
        for v in one_hot
    ]


def cross_entropy(target, pred, eps=1e-12):
    return -sum(t * math.log(p + eps) for t, p in zip(target, pred))


if __name__ == "__main__":
    one_hot = [0, 1, 0, 0]
    predictions = [0.05, 0.85, 0.06, 0.04]

    smoothed = smooth_labels(one_hot, alpha=0.1)
    print("Original one-hot label:", one_hot)
    print("Smoothed label:        ", [round(v, 4) for v in smoothed])

    loss_hard = cross_entropy(one_hot, predictions)
    loss_smooth = cross_entropy(smoothed, predictions)
    print(f"Cross-entropy with hard labels:     {loss_hard:.4f}")
    print(f"Cross-entropy with smoothed labels: {loss_smooth:.4f}")

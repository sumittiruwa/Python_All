"""ML Practice: ROC Curve Points and AUC Computation"""


def roc_curve(y_true, y_scores):
    thresholds = sorted(set(y_scores), reverse=True)
    thresholds = [max(thresholds) + 1] + thresholds + [min(thresholds) - 1]

    points = []
    n_pos = sum(1 for y in y_true if y == 1)
    n_neg = len(y_true) - n_pos

    for t in thresholds:
        tp = sum(1 for y, s in zip(y_true, y_scores) if s >= t and y == 1)
        fp = sum(1 for y, s in zip(y_true, y_scores) if s >= t and y == 0)
        tpr = tp / n_pos if n_pos else 0
        fpr = fp / n_neg if n_neg else 0
        points.append((fpr, tpr))

    return points


def auc(points):
    points = sorted(points)
    area = 0.0
    for i in range(1, len(points)):
        x0, y0 = points[i - 1]
        x1, y1 = points[i]
        area += (x1 - x0) * (y0 + y1) / 2
    return area


if __name__ == "__main__":
    y_true = [1, 0, 1, 1, 0, 1, 0, 0]
    y_scores = [0.9, 0.4, 0.8, 0.7, 0.3, 0.6, 0.55, 0.2]

    points = roc_curve(y_true, y_scores)
    print("ROC points (fpr, tpr):")
    for fpr, tpr in points:
        print(f"  ({fpr:.2f}, {tpr:.2f})")

    print("AUC:", round(auc(points), 4))

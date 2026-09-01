"""ML Practice: Precision-Recall Curve Computation"""


def precision_recall_curve(y_true, y_scores):
    thresholds = sorted(set(y_scores), reverse=True)
    n_pos = sum(1 for y in y_true if y == 1)

    points = []
    for t in thresholds:
        tp = sum(1 for y, s in zip(y_true, y_scores) if s >= t and y == 1)
        fp = sum(1 for y, s in zip(y_true, y_scores) if s >= t and y == 0)
        precision = tp / (tp + fp) if (tp + fp) else 1.0
        recall = tp / n_pos if n_pos else 0.0
        points.append((round(recall, 3), round(precision, 3)))

    return points


def average_precision(points):
    points = sorted(points)
    ap = 0.0
    prev_recall = 0.0
    for recall, precision in points:
        ap += (recall - prev_recall) * precision
        prev_recall = recall
    return ap


if __name__ == "__main__":
    y_true = [1, 0, 1, 1, 0, 1, 0, 0]
    y_scores = [0.9, 0.4, 0.8, 0.7, 0.3, 0.6, 0.55, 0.2]

    points = precision_recall_curve(y_true, y_scores)
    print("Precision-Recall points (recall, precision):")
    for recall, precision in points:
        print(f"  ({recall}, {precision})")

    print("Average precision:", round(average_precision(points), 4))

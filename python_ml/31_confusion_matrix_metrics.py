"""ML Practice: Confusion Matrix, Accuracy, Precision, Recall, F1 Score"""


def confusion_matrix(y_true, y_pred):
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    tn = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 0)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
    return {"TP": tp, "TN": tn, "FP": fp, "FN": fn}


def accuracy(y_true, y_pred):
    correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
    return correct / len(y_true)


def precision(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    denom = cm["TP"] + cm["FP"]
    return cm["TP"] / denom if denom else 0.0


def recall(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    denom = cm["TP"] + cm["FN"]
    return cm["TP"] / denom if denom else 0.0


def f1_score(y_true, y_pred):
    p, r = precision(y_true, y_pred), recall(y_true, y_pred)
    return 2 * p * r / (p + r) if (p + r) else 0.0


if __name__ == "__main__":
    y_true = [1, 0, 1, 1, 0, 1, 0, 0]
    y_pred = [1, 0, 0, 1, 0, 1, 1, 0]

    print("Confusion matrix:", confusion_matrix(y_true, y_pred))
    print("Accuracy:", round(accuracy(y_true, y_pred), 3))
    print("Precision:", round(precision(y_true, y_pred), 3))
    print("Recall:", round(recall(y_true, y_pred), 3))
    print("F1 Score:", round(f1_score(y_true, y_pred), 3))

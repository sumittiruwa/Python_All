"""ML Practice: Multi-Class Confusion Matrix"""


def confusion_matrix(y_true, y_pred, labels=None):
    labels = labels or sorted(set(y_true) | set(y_pred))
    index = {label: i for i, label in enumerate(labels)}
    matrix = [[0] * len(labels) for _ in labels]

    for true, pred in zip(y_true, y_pred):
        matrix[index[true]][index[pred]] += 1

    return matrix, labels


def print_matrix(matrix, labels):
    header = "true\\pred " + " ".join(f"{l:>6}" for l in labels)
    print(header)
    for label, row in zip(labels, matrix):
        print(f"{label:>9} " + " ".join(f"{v:>6}" for v in row))


def per_class_accuracy(matrix, labels):
    total = sum(sum(row) for row in matrix)
    correct = sum(matrix[i][i] for i in range(len(labels)))
    return correct / total


if __name__ == "__main__":
    y_true = ["cat", "dog", "cat", "bird", "dog", "dog", "bird", "cat"]
    y_pred = ["cat", "dog", "dog", "bird", "dog", "cat", "bird", "cat"]

    matrix, labels = confusion_matrix(y_true, y_pred)
    print_matrix(matrix, labels)
    print("Overall accuracy:", round(per_class_accuracy(matrix, labels), 3))

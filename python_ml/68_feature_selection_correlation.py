"""ML Practice: Correlation-Based Feature Selection"""


def pearson_correlation(x, y):
    n = len(x)
    mean_x, mean_y = sum(x) / n, sum(y) / n
    cov = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    std_x = sum((v - mean_x) ** 2 for v in x) ** 0.5
    std_y = sum((v - mean_y) ** 2 for v in y) ** 0.5
    return cov / (std_x * std_y + 1e-9)


def select_by_correlation(X, y, top_k=2):
    n_features = len(X[0])
    scores = []
    for j in range(n_features):
        col = [row[j] for row in X]
        scores.append((j, abs(pearson_correlation(col, y))))

    scores.sort(key=lambda item: item[1], reverse=True)
    selected = [idx for idx, _ in scores[:top_k]]
    return selected, scores


if __name__ == "__main__":
    X = [[1, 10, 3], [2, 9, 3], [3, 8, 4], [4, 7, 2], [5, 6, 5]]
    y = [2, 4, 6, 8, 10]

    selected, scores = select_by_correlation(X, y, top_k=2)
    print("Correlation scores (feature, |r|):", [(i, round(s, 3)) for i, s in scores])
    print("Selected feature indices:", selected)

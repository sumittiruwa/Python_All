"""ML Practice: Linear Discriminant Analysis for 2-Class Classification"""


def class_mean(X):
    n_features = len(X[0])
    return [sum(row[j] for row in X) / len(X) for j in range(n_features)]


def scatter_matrix(X, mean):
    n = len(mean)
    S = [[0.0] * n for _ in range(n)]
    for row in X:
        diff = [row[j] - mean[j] for j in range(n)]
        for i in range(n):
            for j in range(n):
                S[i][j] += diff[i] * diff[j]
    return S


def matrix_add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def solve_2x2(A, b):
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    x0 = (b[0] * A[1][1] - A[0][1] * b[1]) / det
    x1 = (A[0][0] * b[1] - b[0] * A[1][0]) / det
    return [x0, x1]


def lda_direction(X0, X1):
    mean0, mean1 = class_mean(X0), class_mean(X1)
    within_scatter = matrix_add(scatter_matrix(X0, mean0), scatter_matrix(X1, mean1))
    mean_diff = [mean1[i] - mean0[i] for i in range(len(mean0))]
    w = solve_2x2(within_scatter, mean_diff)
    return w, mean0, mean1


def project(x, w):
    return sum(wi * xi for wi, xi in zip(w, x))


if __name__ == "__main__":
    X0 = [[1, 2], [2, 1], [1.5, 1.5], [2, 2]]
    X1 = [[7, 8], [8, 7], [7.5, 7.5], [8, 8]]

    w, mean0, mean1 = lda_direction(X0, X1)
    threshold = (project(mean0, w) + project(mean1, w)) / 2

    print("LDA direction w:", [round(v, 3) for v in w])
    for x in [[1.8, 1.9], [7.7, 7.6], [4.5, 4.5]]:
        score = project(x, w)
        label = 1 if score > threshold else 0
        print(f"{x} -> projection={score:.3f}, class={label}")

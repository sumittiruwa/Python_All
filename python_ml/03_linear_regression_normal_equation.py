"""ML Practice: Linear Regression using the Normal Equation (closed-form solution)"""


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matmul(a, b):
    b_t = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in b_t] for row in a]


def invert_matrix(matrix):
    n = len(matrix)
    identity = [[float(i == j) for j in range(n)] for i in range(n)]
    aug = [row[:] + identity[i] for i, row in enumerate(matrix)]

    for i in range(n):
        pivot = aug[i][i]
        aug[i] = [val / pivot for val in aug[i]]
        for j in range(n):
            if j != i:
                factor = aug[j][i]
                aug[j] = [aug[j][k] - factor * aug[i][k] for k in range(2 * n)]

    return [row[n:] for row in aug]


def normal_equation(X, y):
    X_b = [[1.0] + list(row) for row in X]
    X_t = transpose(X_b)
    y_col = [[val] for val in y]

    theta = matmul(matmul(invert_matrix(matmul(X_t, X_b)), X_t), y_col)
    return [t[0] for t in theta]


if __name__ == "__main__":
    X = [[1], [2], [3], [4], [5]]
    y = [3, 5, 7, 9, 11]

    theta = normal_equation(X, y)
    print("bias:", round(theta[0], 3), "weight:", round(theta[1], 3))

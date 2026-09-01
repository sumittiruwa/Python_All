"""ML Practice: Singular Value Decomposition Basics via Power Iteration"""

import math


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def matmul(a, b):
    b_t = transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in b_t] for row in a]


def matvec(matrix, vec):
    return [sum(row[j] * vec[j] for j in range(len(vec))) for row in matrix]


def normalize(vec):
    norm = math.sqrt(sum(v ** 2 for v in vec)) or 1e-9
    return [v / norm for v in vec]


def top_singular_triplet(A, iterations=200):
    ata = matmul(transpose(A), A)
    v = [1.0] * len(ata)
    for _ in range(iterations):
        v = normalize(matvec(ata, v))

    sigma = math.sqrt(sum(x * y for x, y in zip(v, matvec(ata, v))))
    Av = matvec(A, v)
    u = normalize(Av)

    return u, sigma, v


if __name__ == "__main__":
    A = [[3, 0], [4, 5]]

    u, sigma, v = top_singular_triplet(A)
    print("Matrix A:", A)
    print("Top left singular vector u:", [round(x, 3) for x in u])
    print("Top singular value sigma:", round(sigma, 3))
    print("Top right singular vector v:", [round(x, 3) for x in v])

"""ML Practice: Xavier and He Weight Initialization Schemes"""

import random
import math


def xavier_init(n_in, n_out, seed=1):
    random.seed(seed)
    limit = math.sqrt(6 / (n_in + n_out))
    return [[random.uniform(-limit, limit) for _ in range(n_in)] for _ in range(n_out)]


def he_init(n_in, n_out, seed=1):
    random.seed(seed)
    stddev = math.sqrt(2 / n_in)
    return [[random.gauss(0, stddev) for _ in range(n_in)] for _ in range(n_out)]


def stats(matrix):
    flat = [v for row in matrix for v in row]
    mean = sum(flat) / len(flat)
    variance = sum((v - mean) ** 2 for v in flat) / len(flat)
    return mean, variance ** 0.5


if __name__ == "__main__":
    n_in, n_out = 256, 128

    xavier_weights = xavier_init(n_in, n_out)
    he_weights = he_init(n_in, n_out)

    x_mean, x_std = stats(xavier_weights)
    h_mean, h_std = stats(he_weights)

    print(f"Xavier init: mean={x_mean:.5f}, std={x_std:.5f}")
    print(f"He init:     mean={h_mean:.5f}, std={h_std:.5f}")

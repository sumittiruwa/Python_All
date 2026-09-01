"""ML Practice: Bootstrap Confidence Interval for the Mean"""

import random


def bootstrap_ci(data, n_iterations=1000, ci=95, seed=0):
    random.seed(seed)
    n = len(data)
    means = []

    for _ in range(n_iterations):
        sample = [data[random.randrange(n)] for _ in range(n)]
        means.append(sum(sample) / n)

    means.sort()
    lower_pct = (100 - ci) / 2
    upper_pct = 100 - lower_pct
    lower_idx = int(lower_pct / 100 * n_iterations)
    upper_idx = int(upper_pct / 100 * n_iterations) - 1

    return means[lower_idx], means[upper_idx]


if __name__ == "__main__":
    data = [23, 25, 21, 27, 24, 22, 26, 20, 28, 24]

    mean = sum(data) / len(data)
    lower, upper = bootstrap_ci(data, n_iterations=2000, ci=95)

    print("Sample mean:", round(mean, 3))
    print(f"95% bootstrap CI: [{lower:.3f}, {upper:.3f}]")

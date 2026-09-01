"""ML Practice: Bootstrap Resampling Utility"""

import random


def bootstrap_sample(data, seed=None):
    if seed is not None:
        random.seed(seed)
    n = len(data)
    return [data[random.randrange(n)] for _ in range(n)]


def bootstrap_statistic(data, statistic_fn, n_iterations=100, seed=0):
    random.seed(seed)
    results = []
    for _ in range(n_iterations):
        sample = [data[random.randrange(len(data))] for _ in range(len(data))]
        results.append(statistic_fn(sample))
    return results


if __name__ == "__main__":
    data = [12, 15, 14, 10, 18, 20, 13, 17]

    print("Original data:", data)
    print("One bootstrap sample:", bootstrap_sample(data, seed=1))

    means = bootstrap_statistic(data, lambda s: sum(s) / len(s), n_iterations=200)
    avg_of_means = sum(means) / len(means)
    print(f"Original mean: {sum(data) / len(data):.3f}")
    print(f"Average of {len(means)} bootstrap means: {avg_of_means:.3f}")

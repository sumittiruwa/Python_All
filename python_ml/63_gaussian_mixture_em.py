"""ML Practice: Gaussian Mixture Model fit via EM Algorithm (1D)"""

import math


def gaussian_pdf(x, mean, var):
    var = max(var, 1e-6)
    return (1 / math.sqrt(2 * math.pi * var)) * math.exp(-((x - mean) ** 2) / (2 * var))


def em_gmm(data, k=2, epochs=50, seed_means=None):
    means = seed_means or data[:k]
    variances = [1.0] * k
    weights = [1 / k] * k
    n = len(data)

    for _ in range(epochs):
        responsibilities = []
        for x in data:
            probs = [weights[j] * gaussian_pdf(x, means[j], variances[j]) for j in range(k)]
            total = sum(probs) or 1e-9
            responsibilities.append([p / total for p in probs])

        for j in range(k):
            r_sum = sum(r[j] for r in responsibilities)
            means[j] = sum(r[j] * x for r, x in zip(responsibilities, data)) / r_sum
            variances[j] = sum(r[j] * (x - means[j]) ** 2 for r, x in zip(responsibilities, data)) / r_sum
            weights[j] = r_sum / n

    return means, variances, weights


if __name__ == "__main__":
    data = [1.0, 1.2, 0.9, 1.1, 0.8, 8.0, 8.2, 7.9, 8.1, 7.8]

    means, variances, weights = em_gmm(data, k=2, seed_means=[0.0, 5.0])

    for j in range(2):
        print(f"Component {j}: mean={means[j]:.3f}, var={variances[j]:.3f}, weight={weights[j]:.3f}")

"""ML Practice: Simplified Batch Normalization of Activations"""


def batch_norm(batch, gamma=1.0, beta=0.0, eps=1e-8):
    n_features = len(batch[0])
    means = [sum(row[j] for row in batch) / len(batch) for j in range(n_features)]
    variances = [
        sum((row[j] - means[j]) ** 2 for row in batch) / len(batch)
        for j in range(n_features)
    ]

    normalized = []
    for row in batch:
        norm_row = [
            gamma * (row[j] - means[j]) / (variances[j] + eps) ** 0.5 + beta
            for j in range(n_features)
        ]
        normalized.append(norm_row)

    return normalized, means, variances


if __name__ == "__main__":
    batch = [[1.0, 10.0], [2.0, 20.0], [3.0, 30.0], [4.0, 40.0]]

    normalized, means, variances = batch_norm(batch)
    print("Means:", [round(m, 3) for m in means])
    print("Variances:", [round(v, 3) for v in variances])
    for row in normalized:
        print("Normalized:", [round(v, 3) for v in row])

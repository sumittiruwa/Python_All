"""ML Practice: Hard and Soft Voting Ensemble"""

from collections import Counter


def classifier_a(x):
    prob = 1.0 if x[0] + x[1] > 10 else 0.0
    return prob


def classifier_b(x):
    prob = min(1.0, max(0.0, (x[0] - 3) / 6))
    return prob


def classifier_c(x):
    prob = 1.0 if x[0] > x[1] else 0.0
    return prob


def hard_vote(x, classifiers):
    votes = [1 if c(x) >= 0.5 else 0 for c in classifiers]
    return Counter(votes).most_common(1)[0][0]


def soft_vote(x, classifiers, weights=None):
    weights = weights or [1] * len(classifiers)
    total = sum(weights)
    avg_prob = sum(w * c(x) for w, c in zip(weights, classifiers)) / total
    return 1 if avg_prob >= 0.5 else 0, avg_prob


if __name__ == "__main__":
    classifiers = [classifier_a, classifier_b, classifier_c]
    samples = [[2, 1], [9, 8], [5, 3], [1, 9]]

    for x in samples:
        hard = hard_vote(x, classifiers)
        soft, prob = soft_vote(x, classifiers, weights=[2, 1, 1])
        print(f"{x} -> hard vote: {hard}, soft vote: {soft} (avg prob={prob:.3f})")

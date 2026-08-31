"""ML Practice: Distance and Similarity Metrics used in ML"""

import math


def euclidean_distance(a, b):
    return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))


def manhattan_distance(a, b):
    return sum(abs(a[i] - b[i]) for i in range(len(a)))


def cosine_similarity(a, b):
    dot = sum(a[i] * b[i] for i in range(len(a)))
    norm_a = math.sqrt(sum(v ** 2 for v in a))
    norm_b = math.sqrt(sum(v ** 2 for v in b))
    return dot / (norm_a * norm_b) if norm_a and norm_b else 0.0


def hamming_distance(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [4, 5, 6]

    print("Euclidean:", round(euclidean_distance(a, b), 3))
    print("Manhattan:", manhattan_distance(a, b))
    print("Cosine similarity:", round(cosine_similarity(a, b), 3))
    print("Hamming distance:", hamming_distance("karolin", "kathrin"))

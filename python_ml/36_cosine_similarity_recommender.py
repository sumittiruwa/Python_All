"""ML Practice: Content-Based Recommender using Cosine Similarity on item features"""

import math


def cosine_similarity(a, b):
    dot = sum(a[i] * b[i] for i in range(len(a)))
    norm_a = math.sqrt(sum(v ** 2 for v in a))
    norm_b = math.sqrt(sum(v ** 2 for v in b))
    return dot / (norm_a * norm_b) if norm_a and norm_b else 0.0


def recommend_similar_items(item_features, target_item, top_n=2):
    target_vector = item_features[target_item]
    similarities = {
        item: cosine_similarity(target_vector, vector)
        for item, vector in item_features.items() if item != target_item
    }
    return sorted(similarities.items(), key=lambda pair: pair[1], reverse=True)[:top_n]


if __name__ == "__main__":
    # Features: [action, comedy, romance]
    item_features = {
        "MovieA": [0.9, 0.1, 0.2],
        "MovieB": [0.8, 0.2, 0.1],
        "MovieC": [0.1, 0.9, 0.8],
        "MovieD": [0.2, 0.8, 0.9],
    }

    recommendations = recommend_similar_items(item_features, "MovieA")
    print("Items similar to MovieA:", recommendations)

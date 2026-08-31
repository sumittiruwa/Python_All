"""ML Practice: User-Based Collaborative Filtering for Recommendations"""

import math


def cosine_similarity(a, b):
    common_keys = set(a.keys()) & set(b.keys())
    if not common_keys:
        return 0.0
    dot = sum(a[k] * b[k] for k in common_keys)
    norm_a = math.sqrt(sum(v ** 2 for v in a.values()))
    norm_b = math.sqrt(sum(v ** 2 for v in b.values()))
    return dot / (norm_a * norm_b) if norm_a and norm_b else 0.0


def recommend(user_ratings, target_user, top_n=2):
    similarities = {
        user: cosine_similarity(user_ratings[target_user], user_ratings[user])
        for user in user_ratings if user != target_user
    }

    scores = {}
    for user, sim in similarities.items():
        for item, rating in user_ratings[user].items():
            if item not in user_ratings[target_user]:
                scores[item] = scores.get(item, 0) + sim * rating

    return sorted(scores.items(), key=lambda pair: pair[1], reverse=True)[:top_n]


if __name__ == "__main__":
    user_ratings = {
        "Alice": {"MovieA": 5, "MovieB": 3, "MovieC": 4},
        "Bob": {"MovieA": 4, "MovieB": 2, "MovieD": 5},
        "Carol": {"MovieA": 5, "MovieC": 5, "MovieD": 4},
    }

    recommendations = recommend(user_ratings, "Alice")
    print("Recommendations for Alice:", recommendations)

"""ML Practice: Cosine-Similarity Document Search Engine"""

import math
from collections import Counter


def tokenize(text):
    return text.lower().split()


def build_vocab(documents):
    vocab = set()
    for doc in documents:
        vocab.update(tokenize(doc))
    return sorted(vocab)


def vectorize(text, vocab):
    counts = Counter(tokenize(text))
    return [counts[word] for word in vocab]


def cosine_similarity(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x ** 2 for x in a))
    norm_b = math.sqrt(sum(y ** 2 for y in b))
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot / (norm_a * norm_b)


def search(query, documents, top_k=2):
    vocab = build_vocab(documents + [query])
    query_vec = vectorize(query, vocab)
    scores = [(doc, cosine_similarity(query_vec, vectorize(doc, vocab))) for doc in documents]
    scores.sort(key=lambda item: item[1], reverse=True)
    return scores[:top_k]


if __name__ == "__main__":
    documents = [
        "python is a great programming language",
        "machine learning uses python heavily",
        "cats and dogs are popular pets",
        "deep learning is a subset of machine learning",
    ]

    query = "python machine learning"
    results = search(query, documents, top_k=3)

    print(f"Query: {query!r}")
    for doc, score in results:
        print(f"  score={score:.3f}: {doc!r}")

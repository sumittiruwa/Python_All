"""ML Practice: TF-IDF Vectorizer from Scratch"""

import math
from collections import Counter


def tokenize(text):
    return text.lower().split()


def build_vocab(documents):
    vocab = set()
    for doc in documents:
        vocab.update(tokenize(doc))
    return sorted(vocab)


def term_frequency(document, vocab):
    tokens = tokenize(document)
    counts = Counter(tokens)
    return [counts[word] / len(tokens) for word in vocab]


def inverse_document_frequency(documents, vocab):
    n_docs = len(documents)
    idf = []
    for word in vocab:
        containing = sum(1 for doc in documents if word in tokenize(doc))
        idf.append(math.log((1 + n_docs) / (1 + containing)) + 1)
    return idf


def tfidf_vectorize(documents):
    vocab = build_vocab(documents)
    idf = inverse_document_frequency(documents, vocab)
    vectors = [
        [tf * w for tf, w in zip(term_frequency(doc, vocab), idf)]
        for doc in documents
    ]
    return vectors, vocab


if __name__ == "__main__":
    documents = [
        "the cat sat on the mat",
        "the dog sat on the log",
        "cats and dogs are friends",
    ]

    vectors, vocab = tfidf_vectorize(documents)
    print("Vocabulary:", vocab)
    for doc, vector in zip(documents, vectors):
        print(f"{doc!r} -> {[round(v, 3) for v in vector]}")

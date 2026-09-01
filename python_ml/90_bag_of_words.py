"""ML Practice: Bag-of-Words Text Vectorizer from Scratch"""

from collections import Counter


def tokenize(text):
    return text.lower().split()


def build_vocab(documents):
    vocab = set()
    for doc in documents:
        vocab.update(tokenize(doc))
    return sorted(vocab)


def vectorize(document, vocab):
    counts = Counter(tokenize(document))
    return [counts[word] for word in vocab]


if __name__ == "__main__":
    documents = [
        "the cat sat on the mat",
        "the dog sat on the log",
        "cats and dogs are friends",
    ]

    vocab = build_vocab(documents)
    print("Vocabulary:", vocab)

    for doc in documents:
        vector = vectorize(doc, vocab)
        print(f"{doc!r} -> {vector}")

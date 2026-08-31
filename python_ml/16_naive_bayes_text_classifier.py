"""ML Practice: Naive Bayes Text Classifier (bag-of-words, spam detection style)"""

import math
from collections import defaultdict, Counter


def tokenize(text):
    return text.lower().split()


def train(documents, labels):
    class_word_counts = defaultdict(Counter)
    class_doc_counts = Counter(labels)
    vocabulary = set()

    for doc, label in zip(documents, labels):
        words = tokenize(doc)
        class_word_counts[label].update(words)
        vocabulary.update(words)

    return class_word_counts, class_doc_counts, vocabulary


def predict(text, class_word_counts, class_doc_counts, vocabulary):
    words = tokenize(text)
    total_docs = sum(class_doc_counts.values())
    vocab_size = len(vocabulary)

    best_label, best_score = None, float("-inf")
    for label in class_doc_counts:
        log_prob = math.log(class_doc_counts[label] / total_docs)
        total_words_in_class = sum(class_word_counts[label].values())

        for word in words:
            word_count = class_word_counts[label][word]
            log_prob += math.log((word_count + 1) / (total_words_in_class + vocab_size))

        if log_prob > best_score:
            best_score = log_prob
            best_label = label

    return best_label


if __name__ == "__main__":
    documents = [
        "win money now",
        "cheap loans available",
        "meeting scheduled tomorrow",
        "project deadline reminder",
    ]
    labels = ["spam", "spam", "ham", "ham"]

    class_word_counts, class_doc_counts, vocabulary = train(documents, labels)

    print("Prediction 'free money now':", predict("free money now", class_word_counts, class_doc_counts, vocabulary))
    print("Prediction 'project meeting':", predict("project meeting", class_word_counts, class_doc_counts, vocabulary))

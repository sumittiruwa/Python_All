"""ML Practice: Multinomial Naive Bayes Spam Filter"""

from collections import Counter


def tokenize(text):
    return text.lower().split()


def train(docs, labels):
    class_word_counts = {c: Counter() for c in set(labels)}
    class_totals = {c: 0 for c in set(labels)}
    class_doc_counts = Counter(labels)
    vocab = set()

    for doc, label in zip(docs, labels):
        words = tokenize(doc)
        class_word_counts[label].update(words)
        class_totals[label] += len(words)
        vocab.update(words)

    return class_word_counts, class_totals, class_doc_counts, vocab


def word_prob(word, label, class_word_counts, class_totals, vocab):
    count = class_word_counts[label][word]
    return (count + 1) / (class_totals[label] + len(vocab))


def predict(doc, class_word_counts, class_totals, class_doc_counts, vocab):
    total_docs = sum(class_doc_counts.values())
    best_label, best_score = None, float("-inf")

    for label, doc_count in class_doc_counts.items():
        score = doc_count / total_docs
        for word in tokenize(doc):
            score *= word_prob(word, label, class_word_counts, class_totals, vocab)
        if score > best_score:
            best_label, best_score = label, score

    return best_label


if __name__ == "__main__":
    docs = [
        "win free money now",
        "claim your free prize now",
        "meeting scheduled for tomorrow",
        "please review the attached report",
        "cheap loans and free cash offers",
        "let's catch up over lunch tomorrow",
    ]
    labels = ["spam", "spam", "ham", "ham", "spam", "ham"]

    model = train(docs, labels)

    for test in ["free cash prize now", "schedule tomorrow's report meeting"]:
        print(f"{test!r} -> {predict(test, *model)}")

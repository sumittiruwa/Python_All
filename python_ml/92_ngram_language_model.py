"""ML Practice: N-gram Language Model with Next-Word Prediction"""

from collections import defaultdict, Counter


def tokenize(text):
    return text.lower().split()


def build_ngram_model(corpus, n=2):
    model = defaultdict(Counter)
    for sentence in corpus:
        tokens = tokenize(sentence)
        for i in range(len(tokens) - n + 1):
            context = tuple(tokens[i:i + n - 1])
            next_word = tokens[i + n - 1]
            model[context][next_word] += 1
    return model


def predict_next(model, context):
    context = tuple(context)
    if context not in model:
        return None
    return model[context].most_common(1)[0][0]


def generate(model, start, n_words=5):
    context = list(start)
    result = list(start)
    for _ in range(n_words):
        next_word = predict_next(model, context[-(len(start)):])
        if next_word is None:
            break
        result.append(next_word)
        context.append(next_word)
    return " ".join(result)


if __name__ == "__main__":
    corpus = [
        "i love machine learning",
        "i love deep learning",
        "machine learning is fun",
        "deep learning is powerful",
    ]

    model = build_ngram_model(corpus, n=2)
    print("Next word after 'i':", predict_next(model, ["i"]))
    print("Next word after 'machine':", predict_next(model, ["machine"]))
    print("Generated text:", generate(model, ["i"], n_words=4))

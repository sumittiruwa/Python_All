"""ML Practice: Lexicon-Based Sentiment Scoring"""

POSITIVE_WORDS = {"good", "great", "excellent", "happy", "love", "amazing", "wonderful"}
NEGATIVE_WORDS = {"bad", "terrible", "sad", "hate", "awful", "poor", "disappointing"}


def tokenize(text):
    return text.lower().split()


def sentiment_score(text):
    tokens = tokenize(text)
    pos = sum(1 for word in tokens if word in POSITIVE_WORDS)
    neg = sum(1 for word in tokens if word in NEGATIVE_WORDS)
    return pos - neg


def classify(text):
    score = sentiment_score(text)
    if score > 0:
        return "positive"
    if score < 0:
        return "negative"
    return "neutral"


if __name__ == "__main__":
    reviews = [
        "This movie was great and amazing",
        "The food was terrible and the service was poor",
        "It was an okay experience, nothing special",
        "I love this product, it is wonderful",
    ]

    for review in reviews:
        score = sentiment_score(review)
        print(f"{review!r} -> score={score}, sentiment={classify(review)}")

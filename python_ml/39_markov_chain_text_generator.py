"""ML Practice: Markov Chain based Text Generator"""

import random
from collections import defaultdict


def build_markov_chain(text, order=1):
    words = text.split()
    chain = defaultdict(list)

    for i in range(len(words) - order):
        state = tuple(words[i:i + order])
        next_word = words[i + order]
        chain[state].append(next_word)

    return chain


def generate_text(chain, order, length=20, seed=1):
    random.seed(seed)
    state = random.choice(list(chain.keys()))
    result = list(state)

    for _ in range(length - order):
        next_words = chain.get(state)
        if not next_words:
            break
        next_word = random.choice(next_words)
        result.append(next_word)
        state = tuple(result[-order:])

    return " ".join(result)


if __name__ == "__main__":
    text = "the cat sat on the mat the cat ran on the road the dog sat on the mat"

    chain = build_markov_chain(text, order=2)
    generated = generate_text(chain, order=2, length=15)
    print("Generated text:", generated)

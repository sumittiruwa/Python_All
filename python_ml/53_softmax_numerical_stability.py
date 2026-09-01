"""ML Practice: Naive vs Numerically-Stable Softmax"""

import math


def softmax_naive(logits):
    exps = [math.exp(z) for z in logits]
    total = sum(exps)
    return [e / total for e in exps]


def softmax_stable(logits):
    max_logit = max(logits)
    exps = [math.exp(z - max_logit) for z in logits]
    total = sum(exps)
    return [e / total for e in exps]


if __name__ == "__main__":
    safe_logits = [2.0, 1.0, 0.1]
    print("Naive softmax (safe inputs): ", [round(p, 4) for p in softmax_naive(safe_logits)])
    print("Stable softmax (safe inputs):", [round(p, 4) for p in softmax_stable(safe_logits)])

    large_logits = [1000, 1001, 1002]
    try:
        print("Naive softmax (large inputs):", softmax_naive(large_logits))
    except OverflowError as e:
        print("Naive softmax (large inputs): OverflowError ->", e)
    print("Stable softmax (large inputs):", [round(p, 4) for p in softmax_stable(large_logits)])

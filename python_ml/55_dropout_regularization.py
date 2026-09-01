"""ML Practice: Dropout Regularization Simulation on a Layer"""

import random


def dropout(activations, drop_prob=0.5, seed=None, training=True):
    if not training:
        return activations

    if seed is not None:
        random.seed(seed)

    keep_prob = 1 - drop_prob
    mask = [0 if random.random() < drop_prob else 1 for _ in activations]
    return [a * m / keep_prob for a, m in zip(activations, mask)]


if __name__ == "__main__":
    activations = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]

    print("Original activations:", activations)
    for trial in range(3):
        dropped = dropout(activations, drop_prob=0.4, seed=trial)
        print(f"Trial {trial} (training=True): ", [round(v, 2) for v in dropped])

    print("Inference (training=False):", dropout(activations, drop_prob=0.4, training=False))

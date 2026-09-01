"""ML Practice: Hill Climbing Local Search on a Toy Function"""

import random


def objective(x):
    return -(x ** 2) + 4 * x + 1


def hill_climbing(start, step_size=0.1, iterations=200, seed=1):
    random.seed(seed)
    current = start
    current_value = objective(current)
    history = [(current, current_value)]

    for _ in range(iterations):
        step = random.choice([-step_size, step_size])
        candidate = current + step
        candidate_value = objective(candidate)

        if candidate_value > current_value:
            current, current_value = candidate, candidate_value
            history.append((current, current_value))

    return current, current_value, history


if __name__ == "__main__":
    best_x, best_value, history = hill_climbing(start=-5.0)
    print(f"Start: x=-5.0, value={objective(-5.0):.4f}")
    print(f"Best x found: {best_x:.4f}")
    print(f"Best value: {best_value:.4f}")
    print(f"Number of improving moves: {len(history) - 1}")

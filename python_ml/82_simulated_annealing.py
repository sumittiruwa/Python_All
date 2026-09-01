"""ML Practice: Simulated Annealing Optimizer on a Toy Function"""

import math
import random


def objective(x):
    return (x - 3) ** 2 + math.sin(5 * x)


def simulated_annealing(start, iterations=1000, initial_temp=10.0, cooling=0.995, seed=1):
    random.seed(seed)
    current = start
    current_cost = objective(current)
    best, best_cost = current, current_cost
    temp = initial_temp

    for _ in range(iterations):
        candidate = current + random.uniform(-1, 1)
        candidate_cost = objective(candidate)
        delta = candidate_cost - current_cost

        if delta < 0 or random.random() < math.exp(-delta / max(temp, 1e-9)):
            current, current_cost = candidate, candidate_cost
            if current_cost < best_cost:
                best, best_cost = current, current_cost

        temp *= cooling

    return best, best_cost


if __name__ == "__main__":
    best_x, best_cost = simulated_annealing(start=0.0)
    print(f"Best x found: {best_x:.4f}")
    print(f"Objective value: {best_cost:.4f}")

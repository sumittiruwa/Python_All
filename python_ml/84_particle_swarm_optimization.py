"""ML Practice: Particle Swarm Optimization on a Toy Function"""

import random


def objective(x, y):
    return (x - 3) ** 2 + (y + 2) ** 2


def pso(bounds, n_particles=20, iterations=100, w=0.5, c1=1.5, c2=1.5, seed=1):
    random.seed(seed)
    low, high = bounds

    positions = [[random.uniform(low, high), random.uniform(low, high)] for _ in range(n_particles)]
    velocities = [[0.0, 0.0] for _ in range(n_particles)]
    personal_best = [p[:] for p in positions]
    personal_best_val = [objective(*p) for p in positions]

    global_best = min(personal_best, key=lambda p: objective(*p))
    global_best = global_best[:]

    for _ in range(iterations):
        for i in range(n_particles):
            for d in range(2):
                r1, r2 = random.random(), random.random()
                velocities[i][d] = (
                    w * velocities[i][d]
                    + c1 * r1 * (personal_best[i][d] - positions[i][d])
                    + c2 * r2 * (global_best[d] - positions[i][d])
                )
                positions[i][d] += velocities[i][d]

            value = objective(*positions[i])
            if value < personal_best_val[i]:
                personal_best[i] = positions[i][:]
                personal_best_val[i] = value
                if value < objective(*global_best):
                    global_best = positions[i][:]

    return global_best, objective(*global_best)


if __name__ == "__main__":
    best_pos, best_val = pso(bounds=(-10, 10))
    print(f"Best position: ({best_pos[0]:.4f}, {best_pos[1]:.4f})")
    print(f"Objective value: {best_val:.6f}")

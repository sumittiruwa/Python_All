"""ML Practice: Genetic Algorithm Optimizer on a Toy Function"""

import random
import math


def fitness(x):
    return -((x - 5) ** 2) + 10 * math.cos(x)


def create_population(size, low, high, seed):
    random.seed(seed)
    return [random.uniform(low, high) for _ in range(size)]


def select_parent(population, fitnesses):
    total = sum(f - min(fitnesses) + 1e-6 for f in fitnesses)
    pick = random.uniform(0, total)
    running = 0
    for individual, f in zip(population, fitnesses):
        running += f - min(fitnesses) + 1e-6
        if running >= pick:
            return individual
    return population[-1]


def genetic_algorithm(low, high, pop_size=30, generations=50, mutation_rate=0.2, seed=1):
    random.seed(seed)
    population = create_population(pop_size, low, high, seed)

    for _ in range(generations):
        fitnesses = [fitness(ind) for ind in population]
        new_population = []
        for _ in range(pop_size):
            parent1 = select_parent(population, fitnesses)
            parent2 = select_parent(population, fitnesses)
            child = (parent1 + parent2) / 2
            if random.random() < mutation_rate:
                child += random.uniform(-0.5, 0.5)
            new_population.append(max(low, min(high, child)))
        population = new_population

    best = max(population, key=fitness)
    return best, fitness(best)


if __name__ == "__main__":
    best_x, best_fitness = genetic_algorithm(low=0, high=10)
    print(f"Best x found: {best_x:.4f}")
    print(f"Fitness value: {best_fitness:.4f}")

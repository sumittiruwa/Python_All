"""ML Practice: Epsilon-Greedy Multi-Armed Bandit"""

import random


def pull_arm(true_probs, arm, seed_state):
    return 1 if seed_state.random() < true_probs[arm] else 0


def epsilon_greedy_bandit(true_probs, n_rounds=2000, epsilon=0.1, seed=1):
    rng = random.Random(seed)
    n_arms = len(true_probs)
    counts = [0] * n_arms
    values = [0.0] * n_arms
    total_reward = 0

    for _ in range(n_rounds):
        if rng.random() < epsilon:
            arm = rng.randrange(n_arms)
        else:
            arm = values.index(max(values))

        reward = pull_arm(true_probs, arm, rng)
        counts[arm] += 1
        values[arm] += (reward - values[arm]) / counts[arm]
        total_reward += reward

    return values, counts, total_reward


if __name__ == "__main__":
    true_probs = [0.2, 0.5, 0.75, 0.4]

    values, counts, total_reward = epsilon_greedy_bandit(true_probs)

    print("True probabilities:", true_probs)
    print("Estimated values:  ", [round(v, 3) for v in values])
    print("Times each arm pulled:", counts)
    print("Total reward:", total_reward)
    print("Best arm found:", values.index(max(values)))

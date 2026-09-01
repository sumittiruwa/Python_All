"""ML Practice: Value Iteration for a Markov Decision Process"""

GRID_SIZE = 4
GOAL = (3, 3)
TRAP = (1, 1)
ACTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def reward(state):
    if state == GOAL:
        return 10
    if state == TRAP:
        return -10
    return -1


def next_state(state, action):
    x, y = state
    dx, dy = action
    return max(0, min(GRID_SIZE - 1, x + dx)), max(0, min(GRID_SIZE - 1, y + dy))


def value_iteration(gamma=0.9, theta=1e-4):
    states = [(x, y) for x in range(GRID_SIZE) for y in range(GRID_SIZE)]
    V = {s: 0.0 for s in states}

    while True:
        delta = 0
        for s in states:
            if s in (GOAL, TRAP):
                continue
            best_value = max(reward(next_state(s, a)) + gamma * V[next_state(s, a)] for a in ACTIONS)
            delta = max(delta, abs(best_value - V[s]))
            V[s] = best_value
        if delta < theta:
            break

    policy = {}
    for s in states:
        if s in (GOAL, TRAP):
            continue
        policy[s] = max(ACTIONS, key=lambda a: reward(next_state(s, a)) + gamma * V[next_state(s, a)])

    return V, policy


if __name__ == "__main__":
    V, policy = value_iteration()

    print("State values (row by row):")
    for y in range(GRID_SIZE - 1, -1, -1):
        print(" ".join(f"{V[(x, y)]:6.2f}" for x in range(GRID_SIZE)))

    print("Optimal action from (0,0):", policy[(0, 0)])

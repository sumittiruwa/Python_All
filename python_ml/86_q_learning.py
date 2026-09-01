"""ML Practice: Q-Learning on a Small Grid-World MDP"""

import random

GRID_SIZE = 4
GOAL = (3, 3)
ACTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def step(state, action):
    x, y = state
    dx, dy = action
    nx, ny = max(0, min(GRID_SIZE - 1, x + dx)), max(0, min(GRID_SIZE - 1, y + dy))
    reward = 10 if (nx, ny) == GOAL else -1
    return (nx, ny), reward


def train_q_learning(episodes=2000, alpha=0.1, gamma=0.9, epsilon=0.2, seed=1):
    random.seed(seed)
    Q = {(x, y): [0.0] * len(ACTIONS) for x in range(GRID_SIZE) for y in range(GRID_SIZE)}

    for _ in range(episodes):
        state = (0, 0)
        for _ in range(50):
            if state == GOAL:
                break
            if random.random() < epsilon:
                action_idx = random.randrange(len(ACTIONS))
            else:
                action_idx = Q[state].index(max(Q[state]))

            next_state, reward = step(state, ACTIONS[action_idx])
            best_next = max(Q[next_state])
            Q[state][action_idx] += alpha * (reward + gamma * best_next - Q[state][action_idx])
            state = next_state

    return Q


def extract_policy(Q):
    return {state: ACTIONS[values.index(max(values))] for state, values in Q.items()}


if __name__ == "__main__":
    Q = train_q_learning()
    policy = extract_policy(Q)

    state = (0, 0)
    path = [state]
    for _ in range(10):
        if state == GOAL:
            break
        state, _ = step(state, policy[state])
        path.append(state)

    print("Learned path from (0,0) to goal:", path)

"""ML Practice: HMM Viterbi Decoding for Most Likely State Sequence"""


def viterbi(observations, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    for state in states:
        V[0][state] = start_p[state] * emit_p[state][observations[0]]
        path[state] = [state]

    for t in range(1, len(observations)):
        V.append({})
        new_path = {}

        for state in states:
            best_prob, best_prev = max(
                (V[t - 1][prev] * trans_p[prev][state] * emit_p[state][observations[t]], prev)
                for prev in states
            )
            V[t][state] = best_prob
            new_path[state] = path[best_prev] + [state]

        path = new_path

    final_state = max(states, key=lambda s: V[-1][s])
    return path[final_state], V[-1][final_state]


if __name__ == "__main__":
    states = ["Sunny", "Rainy"]
    observations = ["walk", "shop", "clean"]

    start_p = {"Sunny": 0.6, "Rainy": 0.4}
    trans_p = {
        "Sunny": {"Sunny": 0.7, "Rainy": 0.3},
        "Rainy": {"Sunny": 0.4, "Rainy": 0.6},
    }
    emit_p = {
        "Sunny": {"walk": 0.6, "shop": 0.3, "clean": 0.1},
        "Rainy": {"walk": 0.1, "shop": 0.4, "clean": 0.5},
    }

    best_path, probability = viterbi(observations, states, start_p, trans_p, emit_p)
    print("Observations:", observations)
    print("Most likely weather sequence:", best_path)
    print(f"Sequence probability: {probability:.6f}")

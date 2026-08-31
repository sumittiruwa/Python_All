"""ML Practice: One-Hot Encoding for Categorical Features"""


def one_hot_encode(categories):
    unique_values = sorted(set(categories))
    index_map = {value: i for i, value in enumerate(unique_values)}

    encoded = []
    for category in categories:
        vector = [0] * len(unique_values)
        vector[index_map[category]] = 1
        encoded.append(vector)

    return encoded, unique_values


if __name__ == "__main__":
    colors = ["red", "green", "blue", "green", "red"]

    encoded, categories = one_hot_encode(colors)
    print("Categories:", categories)
    for color, vector in zip(colors, encoded):
        print(f"{color}: {vector}")

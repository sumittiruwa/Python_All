# Decision Tree without using any library

import math


# Calculate Entropy
def entropy(data):
    total = len(data)
    counts = {}

    for row in data:
        label = row[-1]
        counts[label] = counts.get(label, 0) + 1

    result = 0

    for count in counts.values():
        probability = count / total
        result -= probability * math.log2(probability)

    return result


# Calculate Information Gain
def information_gain(data, index):
    total_entropy = entropy(data)

    groups = {}

    for row in data:
        key = row[index]
        groups.setdefault(key, []).append(row)

    weighted_entropy = 0

    for group in groups.values():
        weighted_entropy += (len(group) / len(data)) * entropy(group)

    return total_entropy - weighted_entropy


# Dataset
data = [
    ['Sunny', 'No'],
    ['Sunny', 'No'],
    ['Overcast', 'Yes'],
    ['Rainy', 'Yes'],
    ['Rainy', 'Yes'],
    ['Rainy', 'No'],
    ['Overcast', 'Yes'],
    ['Sunny', 'No'],
    ['Sunny', 'Yes'],
    ['Rainy', 'Yes']
]


print("Decision Tree")
print("----------------")

print("Entropy:", entropy(data))

gain = information_gain(data, 0)

print("Information Gain:", gain)

if gain > 0:
    print("Best attribute: Weather")
else:
    print("No useful attribute found")
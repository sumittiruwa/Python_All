numbers = [10, 20, 30, 40, 50]

min_val = min(numbers)
max_val = max(numbers)

normalized = []

for x in numbers:
    norm = (x - min_val) / (max_val - min_val)
    normalized.append(norm)

print("Original:", numbers)
print("Normalized:", normalized)
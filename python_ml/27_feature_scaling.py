"""ML Practice: Feature Scaling - Standardization and Min-Max Normalization"""


def standardize(values):
    mean = sum(values) / len(values)
    variance = sum((v - mean) ** 2 for v in values) / len(values)
    stdev = variance ** 0.5 or 1e-9
    return [(v - mean) / stdev for v in values]


def min_max_normalize(values):
    min_val, max_val = min(values), max(values)
    range_val = (max_val - min_val) or 1e-9
    return [(v - min_val) / range_val for v in values]


if __name__ == "__main__":
    data = [10, 20, 30, 40, 50]

    print("Original:", data)
    print("Standardized:", [round(v, 3) for v in standardize(data)])
    print("Min-Max Normalized:", [round(v, 3) for v in min_max_normalize(data)])

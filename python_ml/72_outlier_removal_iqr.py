"""ML Practice: IQR-based Outlier Removal"""


def percentile(sorted_values, p):
    idx = p / 100 * (len(sorted_values) - 1)
    lower = int(idx)
    upper = min(lower + 1, len(sorted_values) - 1)
    frac = idx - lower
    return sorted_values[lower] + frac * (sorted_values[upper] - sorted_values[lower])


def iqr_bounds(values):
    sorted_values = sorted(values)
    q1 = percentile(sorted_values, 25)
    q3 = percentile(sorted_values, 75)
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr


def remove_outliers(values):
    lower, upper = iqr_bounds(values)
    return [v for v in values if lower <= v <= upper], lower, upper


if __name__ == "__main__":
    data = [12, 14, 13, 15, 12, 13, 14, 90, 11, 13, -60, 14, 15]

    cleaned, lower, upper = remove_outliers(data)
    print("Original data:", data)
    print(f"IQR bounds: [{lower:.2f}, {upper:.2f}]")
    print("Cleaned data:", cleaned)

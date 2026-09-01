"""ML Practice: Mean/Median/Mode Imputation for Missing Values"""

from collections import Counter


def impute_mean(column):
    values = [v for v in column if v is not None]
    mean = sum(values) / len(values)
    return [v if v is not None else mean for v in column]


def impute_median(column):
    values = sorted(v for v in column if v is not None)
    mid = len(values) // 2
    median = values[mid] if len(values) % 2 else (values[mid - 1] + values[mid]) / 2
    return [v if v is not None else median for v in column]


def impute_mode(column):
    values = [v for v in column if v is not None]
    mode = Counter(values).most_common(1)[0][0]
    return [v if v is not None else mode for v in column]


if __name__ == "__main__":
    age = [25, None, 30, 28, None, 22]
    income = [50000, 52000, None, 48000, 51000, None]
    category = ["a", "b", "a", None, "a", "b"]

    print("Age (mean imputed):   ", impute_mean(age))
    print("Income (median imputed):", impute_median(income))
    print("Category (mode imputed):", impute_mode(category))

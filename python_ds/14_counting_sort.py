"""DSA Practice: Counting Sort (for non-negative integers)"""


def counting_sort(arr):
    if not arr:
        return []
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    result = []
    for value, freq in enumerate(count):
        result.extend([value] * freq)

    return result


if __name__ == "__main__":
    numbers = [4, 2, 2, 8, 3, 3, 1]
    print("Original:", numbers)
    print("Sorted:", counting_sort(numbers))

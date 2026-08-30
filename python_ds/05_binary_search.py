"""
DSA Practice: Binary Search
Iterative and recursive implementations on a sorted array. O(log n).
"""


def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


if __name__ == "__main__":
    sorted_numbers = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72]

    target = 23
    print(f"Iterative search for {target}:", binary_search_iterative(sorted_numbers, target))
    print(f"Recursive search for {target}:", binary_search_recursive(sorted_numbers, target))

    target = 100
    print(f"Iterative search for {target}:", binary_search_iterative(sorted_numbers, target))

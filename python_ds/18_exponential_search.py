"""DSA Practice: Exponential Search on a sorted array"""


def binary_search(arr, target, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def exponential_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == target:
        return 0

    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    return binary_search(arr, target, i // 2, min(i, n - 1))


if __name__ == "__main__":
    sorted_numbers = [2, 4, 8, 16, 32, 64, 128, 256]
    print("Index of 64:", exponential_search(sorted_numbers, 64))
    print("Index of 100:", exponential_search(sorted_numbers, 100))

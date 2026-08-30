"""DSA Practice: Ternary Search on a sorted array"""


def ternary_search(arr, target, low, high):
    if low > high:
        return -1

    mid1 = low + (high - low) // 3
    mid2 = high - (high - low) // 3

    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2

    if target < arr[mid1]:
        return ternary_search(arr, target, low, mid1 - 1)
    elif target > arr[mid2]:
        return ternary_search(arr, target, mid2 + 1, high)
    else:
        return ternary_search(arr, target, mid1 + 1, mid2 - 1)


if __name__ == "__main__":
    sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    print("Index of 9:", ternary_search(sorted_numbers, 9, 0, len(sorted_numbers) - 1))
    print("Index of 4:", ternary_search(sorted_numbers, 4, 0, len(sorted_numbers) - 1))

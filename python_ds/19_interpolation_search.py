"""DSA Practice: Interpolation Search on a uniformly distributed sorted array"""


def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if arr[high] == arr[low]:
            if arr[low] == target:
                return low
            return -1

        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


if __name__ == "__main__":
    sorted_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    print("Index of 70:", interpolation_search(sorted_numbers, 70))
    print("Index of 100:", interpolation_search(sorted_numbers, 100))

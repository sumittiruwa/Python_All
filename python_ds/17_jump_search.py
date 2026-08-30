"""DSA Practice: Jump Search on a sorted array"""

import math


def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1


if __name__ == "__main__":
    sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print("Index of 13:", jump_search(sorted_numbers, 13))
    print("Index of 4:", jump_search(sorted_numbers, 4))

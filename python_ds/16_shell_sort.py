"""DSA Practice: Shell Sort"""


def shell_sort(arr):
    arr = arr.copy()
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

    return arr


if __name__ == "__main__":
    numbers = [12, 34, 54, 2, 3]
    print("Original:", numbers)
    print("Sorted:", shell_sort(numbers))

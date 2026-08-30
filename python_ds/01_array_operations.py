"""
DSA Practice: Array Operations
Covers traversal, insertion, deletion, and searching in a Python list (array).
"""


def insert_at(arr, index, value):
    arr.insert(index, value)
    return arr


def delete_at(arr, index):
    if 0 <= index < len(arr):
        arr.pop(index)
    return arr


def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def reverse_array(arr):
    return arr[::-1]


def find_max_min(arr):
    return max(arr), min(arr)


if __name__ == "__main__":
    numbers = [5, 3, 8, 1, 9, 2]
    print("Original array:", numbers)

    insert_at(numbers, 2, 100)
    print("After insert:", numbers)

    delete_at(numbers, 0)
    print("After delete:", numbers)

    print("Index of 9:", linear_search(numbers, 9))
    print("Reversed:", reverse_array(numbers))
    print("Max, Min:", find_max_min(numbers))

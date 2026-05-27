# Binary search - divide and conquer (used in ai)

def binary_search(arr, target, lo=0, hi=None):
    if hi is None: hi = len(arr) - 1
    if lo > hi: return -1
    mid = (lo + hi) //2
    if arr[mid] == target: return mid
    elif arr[mid] < target:
        return binary_search(arr,target,mid+1,hi)
    else:
        return binary_search(arr, target,lo,mid-1)

print(factorial(6))
print([fib(i) for i in range(8)])

arr = [1, 2, 3, 45, 67, 88]
print(binary_search(arr, 23))
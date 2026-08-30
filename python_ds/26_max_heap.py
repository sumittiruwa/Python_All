"""DSA Practice: Max Heap using Python's heapq (via negation)"""

import heapq


class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        heapq.heappush(self.heap, -value)

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")
        return -heapq.heappop(self.heap)

    def peek(self):
        if not self.heap:
            raise IndexError("peek from empty heap")
        return -self.heap[0]


if __name__ == "__main__":
    heap = MaxHeap()
    for value in [5, 3, 8, 1, 9, 2]:
        heap.push(value)

    print("Max element:", heap.peek())
    sorted_desc = [heap.pop() for _ in range(6)]
    print("Values popped in descending order:", sorted_desc)

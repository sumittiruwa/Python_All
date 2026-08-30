"""DSA Practice: Min Heap implemented from scratch"""


class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, i):
        return (i - 1) // 2

    def _left(self, i):
        return 2 * i + 1

    def _right(self, i):
        return 2 * i + 2

    def push(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def _sift_up(self, i):
        while i > 0 and self.heap[self._parent(i)] > self.heap[i]:
            parent = self._parent(i)
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def pop(self):
        if not self.heap:
            raise IndexError("pop from empty heap")
        min_val = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self._sift_down(0)
        return min_val

    def _sift_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            left, right = self._left(i), self._right(i)
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest


if __name__ == "__main__":
    heap = MinHeap()
    for value in [5, 3, 8, 1, 9, 2]:
        heap.push(value)

    sorted_values = [heap.pop() for _ in range(6)]
    print("Values popped in sorted order:", sorted_values)

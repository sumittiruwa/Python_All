"""
DSA Practice: Queue (FIFO)
Implemented using collections.deque for O(1) enqueue/dequeue.
"""

from collections import deque


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.popleft()

    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")

    print("Front element:", q.front())
    print("Dequeued:", q.dequeue())
    print("Queue size:", q.size())

    while not q.is_empty():
        print("Dequeued:", q.dequeue())

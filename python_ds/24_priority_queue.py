"""DSA Practice: Priority Queue using heapq"""

import heapq


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty priority queue")
        return heapq.heappop(self.heap)[1]

    def is_empty(self):
        return len(self.heap) == 0


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push("low priority task", 5)
    pq.push("urgent task", 1)
    pq.push("medium task", 3)

    while not pq.is_empty():
        print("Processing:", pq.pop())

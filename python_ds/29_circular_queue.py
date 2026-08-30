"""DSA Practice: Circular Queue with fixed capacity"""


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front_index = 0
        self.rear_index = -1
        self.count = 0

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("queue is full")
        self.rear_index = (self.rear_index + 1) % self.capacity
        self.queue[self.rear_index] = item
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self.queue[self.front_index]
        self.front_index = (self.front_index + 1) % self.capacity
        self.count -= 1
        return item

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity


if __name__ == "__main__":
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    print("Is full:", cq.is_full())

    print("Dequeued:", cq.dequeue())
    cq.enqueue(4)
    print("Dequeued:", cq.dequeue())
    print("Dequeued:", cq.dequeue())
    print("Dequeued:", cq.dequeue())

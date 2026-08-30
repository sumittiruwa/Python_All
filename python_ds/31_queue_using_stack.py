"""DSA Practice: Implement a Queue using two Stacks"""


class QueueUsingStack:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("dequeue from empty queue")
        return self.out_stack.pop()

    def is_empty(self):
        return not self.in_stack and not self.out_stack


if __name__ == "__main__":
    q = QueueUsingStack()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Dequeued:", q.dequeue())
    q.enqueue(4)
    print("Dequeued:", q.dequeue())
    print("Dequeued:", q.dequeue())
    print("Dequeued:", q.dequeue())

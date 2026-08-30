"""DSA Practice: Implement a Stack using two Queues"""

from collections import deque


class StackUsingQueue:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, item):
        self.q2.append(item)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1:
            raise IndexError("pop from empty stack")
        return self.q1.popleft()

    def top(self):
        if not self.q1:
            raise IndexError("top from empty stack")
        return self.q1[0]

    def is_empty(self):
        return len(self.q1) == 0


if __name__ == "__main__":
    s = StackUsingQueue()
    s.push(1)
    s.push(2)
    s.push(3)

    print("Top:", s.top())
    print("Popped:", s.pop())
    print("Popped:", s.pop())
    print("Is empty:", s.is_empty())

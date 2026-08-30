"""DSA Practice: Double-Ended Queue (Deque)"""

from collections import deque


if __name__ == "__main__":
    dq = deque()

    dq.append(10)
    dq.append(20)
    dq.appendleft(5)
    print("Deque after appends:", list(dq))

    dq.pop()
    print("After pop (right):", list(dq))

    dq.popleft()
    print("After popleft:", list(dq))

    dq.extend([30, 40])
    dq.extendleft([1, 2])
    print("After extend/extendleft:", list(dq))

    dq.rotate(2)
    print("After rotate(2):", list(dq))

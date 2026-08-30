"""
DSA Practice: Stack (LIFO)
Implemented using a Python list, plus a classic balanced-parentheses check.
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def is_balanced(expression):
    stack = Stack()
    pairs = {")": "(", "]": "[", "}": "{"}

    for char in expression:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Top element:", s.peek())
    print("Popped:", s.pop())
    print("Stack size:", s.size())

    print("Balanced '(a+b)*(c-d)':", is_balanced("(a+b)*(c-d)"))
    print("Balanced '(a+b]':", is_balanced("(a+b]"))

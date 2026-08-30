"""
DSA Practice: Singly Linked List
Covers insertion at end, deletion by value, traversal, and reversal.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


if __name__ == "__main__":
    ll = LinkedList()
    for value in [1, 2, 3, 4, 5]:
        ll.append(value)

    print("Linked list:", ll.to_list())

    ll.delete(3)
    print("After deleting 3:", ll.to_list())

    ll.reverse()
    print("After reversal:", ll.to_list())

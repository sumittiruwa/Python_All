"""DSA Practice: Doubly Linked List"""


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False

    def to_list_forward(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def to_list_backward(self):
        result = []
        current = self.tail
        while current:
            result.append(current.data)
            current = current.prev
        return result


if __name__ == "__main__":
    dll = DoublyLinkedList()
    for value in [1, 2, 3, 4]:
        dll.append(value)

    print("Forward:", dll.to_list_forward())
    print("Backward:", dll.to_list_backward())

    dll.delete(2)
    print("After deleting 2 (forward):", dll.to_list_forward())

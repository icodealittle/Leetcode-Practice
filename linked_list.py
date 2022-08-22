"""
Why does the size change when using a doubly linked list vs a singly linked list?
"""

class SNode:
    def __init__(self, data):
        self.next = None
        self.data = data


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = SNode(data)
        else:
            # Create a copy of the head node
            copy = self.head  # Make a copy of the head node
            # Go through all the items in the head node until node.next = None
            while copy.next is not None:
                copy = copy.next
            # Copy.next is None
            copy.next = SNode(data)
            # Create a new node at the None position in the Linked List
            # Put copy.next where head is None

    def size(self):
        copy = self.head
        count = 0
        while copy is not None:
            count += 1
            copy = copy.next
        return count


class DNode:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        # Insert an item into the empty head
        if self.head is None:
            self.head = DNode(data)
        # insert an item to a non empty head node
        copy = self.head
        while copy.next is not None:
            copy = copy.next
        copy.next = DNode(data)
        copy.next.prev = copy

    def size(self):
        # Copy
        copy = self.head
        count = 0
        while copy.next is not None:
            copy = copy.next
            count += 1
        return count

    def sizeS(self):
        copy = self.head
        count = 0
        while copy is not None:
            count += 1
            copy = copy.next
        return count



if __name__ == '__main__':
    item = SinglyLinkedList()
    item.add("1")
    item.add("1")
    print(item.sizeS())
    item.add("1")
    print(item.sizeS())

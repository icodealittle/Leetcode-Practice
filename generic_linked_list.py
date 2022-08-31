# https://stackoverflow.com/questions/6725868/generics-templates-in-python
from typing import Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.next = None


class LinkedList(Generic[T]):
    def __init__(self):
        self.head = None
        self.tail = None

    def size(self):
        count = 0
        copy = self.head
        while copy is not None:
            count += 1
            copy = copy.next
        return count

    def is_empty(self):
        return self.size() == 0

    def recursive_add(self, data: Node, node: Node):
        if self.is_empty():
            self.head = Node(data)
            return
        # go forward
        elif node.next is not None:
            node.next = data
        return self.recursive_add(data, node)

    def shallow(self, new_node: Node, curr: Node):
        if self.is_empty():
            self.head = new_node
            return

        elif not curr.next:
            curr.next = new_node
            return
        return self.shallow(new_node, curr.next)

    def add(self, data: T):
        self.shallow(Node(data), self.head)

    def add_i(self, data: T):
        if self.head is None:
            self.head = Node(data)
        copy = self.head
        while copy.next is not None:
            copy = copy.next
        # Copy.next is none
        copy.next = Node(data)

    def remove(self, data: T):
        copy = self.head
        while copy is not None:
            if copy.data == data:
                break
            prev = copy
            copy = copy.next
            prev.next = copy.next
            copy = None
        # Copy is None


if __name__ == '__main__':
    item = LinkedList()
    item.add("H")
    # print(item.is_empty())
    item.add("I")
    print(item.size())
    item.remove("I")
    print(item.size())
    # item.add("J")
    # print(item.size())
    # print(item.is_empty())

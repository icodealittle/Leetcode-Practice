# https://stackoverflow.com/questions/6725868/generics-templates-in-python
from typing import Generic, TypeVar

T = TypeVar("T")
Z = TypeVar("Z")


class Queue(Generic[T]):
    def __init__(self):
        self.data = []

    def deque(self, data):
        '''
        pop from the front
        '''
        self.data.pop(0)

    def enque(self, data):
        '''
        Add to the back
        '''
        self.data.insert(-1, data)

    def size(self):
        return len(self.data)

    def remove(self, key: T):
        '''
        remove at any location
        '''
        if key in self.data:
            self.data.remove(key)
        else:
            raise Exception("Broken!")

    def is_empty(self):
        return self.size() == 0


class Stack(Generic[Z]):
    def __init__(self):
        """
        FIFO
        """
        self.data = []

    def push(self, data: Z):
        return self.data.append(data)

    def pop(self):
        if self.is_empty():
            return
        self.data.pop()

    def peek(self):
        return self.data[0]

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0


if __name__ == '__main__':
    q = Queue()
    s = Stack()

    q.enque("B")
    q.enque("C")
    q.deque("B")
    print(q.is_empty())
    print(q.size())

    s.push("A")
    s.push("B")
    s.push("C")
    s.pop()
    print(s.size())
    print(s.peek())
    print(s.size())

from dataclasses import dataclass


class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data
        self.prev = None
        
class SortedLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        
    def add(self, data):
        # if self.head is None:
        #     self.head = Node(data)
        # copy = self.head
        # newNode = Node(data)
        # while copy is not None:
        
        if self.head is None:
            copy = Node(data)
            copy.data = data
            self.head = copy
            return 
        
        if self.head.data > data:
            copy = Node(data)
            copy.data = data
            copy.next = self.head
            self.head = copy
            return
        
        while self.head.next is not None:
            if self.head.next.data > data:
                break
            copy = self.head.next
        newNode = Node(data)
        newNode.data = data
        newNode.next = self.head.next
        self.head.next = newNode
        return
    
if __name__ == '__main__':
    item = SortedLinkedList()
    item.add(8)
    item.add(7)
    item.add(4)
    item.add(6)
    

                        
        
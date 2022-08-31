class RNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class RLinkedList:
    #Think as recusive + other IDE boolean method
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    def add(self, data):
        if self.tail:
            self.tail.next = RNode(data)
            self.tail = self.tail.next
        else:
            self.head = self.tail = RNode(data)
            return self.add(self.head)
    
    def size(self):
        copy = self.head
        count = 0
        
        while copy is not None:
            count += 1
            copy = copy.next
        return count
    

if __name__ == '__main__':
    item = RLinkedList()
    item.add(3)
    item.add(10)
    item.add(11)
    print(item.size())
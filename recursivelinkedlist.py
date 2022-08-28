class RNode:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class RecursiveLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data, flip=True):
        if flip:
            if self.head is None:
                self.head = RNode(data)
            else:
                # self.head is not None
                self.head = self.head.next
                pcopy = self.head
                self.head.prev = pcopy
                return self.add(data, flip)

    def size(self):
        if self.head is None:
            return 0
        else:
            self.head = self.head.next
            return 1 + self.size()


    def size_I(self):
        count = 0
        copy = self.head
        if self.head is not None:
            count+=1
        return count

    def i_remove(self):
        pass


if __name__ == '__main__':
    item = RecursiveLinkedList()
    item.add("Hello", True)
    item.add("Hello1", True)
    item.add("Hello2", True)
    print(item.size())
    #print(item.size_I())

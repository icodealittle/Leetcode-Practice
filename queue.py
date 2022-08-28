class QueueT:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def deque(self):
        if self.is_empty():
            pass
        else:
            return self.data.pop()

    def enque(self, key):
        self.data.insert(-1, key)

    def size(self):
        return len(self.data)

    def remove(self, key):
        if self.is_empty():
            pass
        for items in self.data:
            if items == key:
                self.data.remove(key)


if __name__ == '__main__':
    item = QueueT()
    item.enque("BOB")
    item.enque("MARLEY")
    item.remove("BOB")
    print(item.size())

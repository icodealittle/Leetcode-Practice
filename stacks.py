class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        """
        Check if the data is empty of not
        """
        if len(self.data) <= 0:
            pass
        else:
            return self.data.pop()

    def peek(self):
        return self.data[-1]

    def size(self):
        return len(self.data)



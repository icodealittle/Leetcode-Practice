# https://medium.com/@hiimdaosui/remove-linked-list-elements-6ec6b7560327
class RNode:
    def __init__(self, data):
        self.next = None
        # self.prev = None
        self.data = data
        self.next = None


class RecursiveLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def traverse(self):
        copy = self.head
        while copy is not None:
            print(copy.data)
            copy = copy.next

    def is_empty(self):
        return self.size() == 0

    def add(self, item):
        # Send in new node with data and the head node
        self.add_recur(RNode(item), self.head)

    def add_recur(self, new_node, curr):
        if self.is_empty():
            self.head = new_node
            return

        elif not curr.next:
            curr.next = new_node
            return
        return self.add_recur(new_node, curr.next)


    def size(self):
        copy = self.head
        count = 0
        while copy is not None:
            count += 1
            #print(copy.data)
            copy = copy.next
        return count

    def remove(self, key):
        """
        @param: key -> the data on the target node
        """
        # Go through the list and find the correct node
        # take a copy of the prev node and next node of the node we remove
        # set copy.prev == copy.next, target.next, target.prev
        # return the new list and update head
        # There needs to be a special case for the head node
        copy = self.head
        rest = self.head
        if copy is not None:
            if copy.data == key:
                self.head = copy.next
        while copy is not None:
            if copy.data == key:
                break
            prev = copy
            copy = copy.next
            prev.next = copy.next
            copy = None






if __name__ == '__main__':
    item = RecursiveLinkedList()
    print(item.is_empty())
    item.add("Hello")
    item.add("Hello1")
    item.add("Hello2")
    item.remove("Hello")
    item.traverse()


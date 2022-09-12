"""
Sorted LL
"""


class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
        self.prev = None


class SortedLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        #[ 1, 3  5, 6, 8] > 5
        # If the head node is null
        if self.head is None:
            self.head = Node(data)
            return
        # If the data is smaller than the head node
        copy = self.head
        new_node = Node(data)
        if copy.data > new_node.data:
            save = copy
            copy = new_node
            copy.next = save

        while copy is not None:
            if new_node.data > copy.data:
                if copy.next is not None:
                    if copy.next.data < new_node.data:
                        copy = copy.next
                    elif copy.next.data > new_node.data:
                        # We know that copy.next is greater than
                        # Put it between copy and copy.next
                        # [2, 5 7 None] >5
                        if copy.next.next is None:
                            save = copy.next
                            copy.next = new_node
                            copy.next.next = save
                            return
                        else:
                            # copy.next.next is not None
                            save = copy.next.next
                            place = copy.next
                            copy.next = new_node
                            copy.next.next = place
                            copy.next.next.next = save
                            return
                    else:
                        # The data is the same number
                        save = copy.next
                        copy.next = new_node
                        copy.next.next = save
                        return
                else:
                    # copy.next is None
                    copy.next = new_node
                    return
            elif new_node.data < copy.data:
                # If the input data is smaller than the head node
                #[ 1 , 5]
                if copy.next is not None:
                    if copy.next.data < new_node.data:
                        copy = copy.next
                    elif copy.next.data > new_node.data:
                        # [ 2, 5] > 4
                        save = copy.next
                        copy.next = new_node
                        copy.next.next = save
                        return
                else:
                    # [ 2, None] > 4
                    copy.next = new_node
                    return

                save = copy
                copy = new_node
                copy.next = save
            elif new_node.data == copy.data:
                save = copy.next
                copy.next = new_node
                copy.next.next = save
            else:
                console.log("ERROR")


    def add2(self, data):
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
        copy = self.head
        while copy.next is not None:
            if copy.next.data > data:
                break
            copy = copy.next

        newNode = Node(data)
        newNode.data = data
        newNode.next = self.head.next
        self.head.next = newNode
        return

    def print(self):
        copy = self.head
        count = 0
        arr = []
        while copy is not None:
            count += 1
            arr.append(copy.data)
            copy = copy.next
        return count, arr




    def remove(self):
        pass


if __name__ == '__main__':
    item = SortedLL()

    item.add(1)
    item.add(3)
    item.add(2)
    item.add(3)
    item.add(4)
    item.add(7)
    item.add(3)
    '''
    item.add2(1)
    item.add2(3)
    item.add2(2)
    item.add2(5)
    item.add2(2)
    item.add2(0)
    '''
    count, arr = item.print()
    print(count)
    print(arr)



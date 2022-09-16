class BSTNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data: int):
        if self.root is None:
            self.root = BSTNode(data)
            return
        else:
            self.rec_add(BSTNode(data), self.root)

    def rec_add(self, new_node, current_node):
        # Check right
        if current_node.data > new_node.data:
            if current_node.left is not None:
                return self.rec_add(new_node=new_node, current_node=current_node.left)
            else:
                # Current.left is None
                current_node.left = new_node
        elif current_node.data < new_node.data:
            if current_node.right is not None:
                return self.rec_add(new_node=new_node, current_node=current_node.right)
            else:
                # current_node.right is None
                current_node.right = new_node

    def remove(self) -> int:
        pass

    def find(self, key) -> bool:
        lst = self.traverse()
        if key in lst:
            return True
        else:
            return False

    def binary_search(self, key):
        lst = self.sort(self.traverse())
        start = 0
        end = len(lst)
        mid = start + end // 2
        def bin_search(lst, mid, start, end, key):
            if start > end:
                return -1
            if lst[mid] == key:
                return mid
            elif key > lst[mid]:
                start = mid
                mid = start + end // 2
                return bin_search(lst, mid, start, end, key)
            elif lst[mid] > key:
                end = mid
                mid = start + end // 2
                return bin_search(lst, mid, start, end, key)
        return bin_search(lst, mid, start, end, key)

    def traverse(self) -> []:
        lst = []
        copy = self.root
        if copy is None:
            return None

        def rec_traverse(copy):
            lst.append(copy.data)
            if copy:
                if copy.left is not None:
                    rec_traverse(copy.left)
                if copy.right is not None:
                    rec_traverse(copy.right)

        rec_traverse(copy)
        return lst


    def sort(self, lst:[]) -> []:
        # Sort in place bubble sort list
        # [2,1,4,5]
        end = len(lst)
        for i in range(len(lst)):
            if i + 1 < end:
                if lst[i] > lst[i + 1]:
                    hold = lst[i]
                    lst[i] = lst[i + 1]
                    lst[i + 1] = hold
        return lst




if __name__ == '__main__':
    item = BST()
    #print(item.sort([2, 1, 4, 5]))
    item.insert(2)
    item.insert(4)
    item.insert(1)
    item.insert(5)
    print(item.find(4))
    print(item.find(2))
    print(item.find(0.9))
    print(item.binary_search(2))
    print(item.traverse())


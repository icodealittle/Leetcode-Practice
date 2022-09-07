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

    def is_empty(self):
        return self.size() == 0


class TreeNode:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None

    def traverse(self):
        """
        1) Create an empty stack S.
        2) Initialize current node as root
        3) Push the current node to S and set current = current->left until current is NULL
        4) If current is NULL and stack is not empty then
        a) Pop the top item from stack.
        b) Print the popped item, set current = popped_item->right
        c) Go to step 3.
        5) If current is NULL and stack is empty then we are done.
        """
        s = Stack()
        current_node = self.root
        while True:
            if current_node is not None:
                s.push(current_node)
                current_node = current_node.left
            elif current_node is None and not s.is_empty():
                current_node = s.pop()
                print(current_node.data)
                current_node = current_node.right
            else:
                break

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self.insert_rec(TreeNode(data), self.root)

    def it_insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            return

        # The root is not none
        copy = self.root
        stop = True

        while stop:  # Check if we should go left of right
            if data < copy.data:
                if copy.left is not None:
                    copy = copy.left
                else:
                    copy.left = TreeNode(data)
                    stop = False
            else:
                # Data is bigger than the current node
                if copy.right is not None:
                    copy = copy.right
                else:
                    copy.right = TreeNode(data)
                    stop = False

    def insert_rec(self, data, node):
        """
        Check the root
        Check left if not right
        >1
        >
        """
        # Traverse from the root checking left and right to see where the data fits
        # Left is smaller--right is bigger

        # 3
        # <1
        # <2     #<3
        # <4

        if data.data < node.data:
            if node.left is not None:
                return self.insert_rec(data, node.left)
            else:
                node.left = data
        else:
            if node.right is not None:
                return self.insert_rec(data, node.right)
            else:
                node.right = data

    def remove(self):
        pass

    def print_tree(self):
        pass

    def size(self):
        pass

    # def travers_re(seft):

    #     self.traverOder

    def recursive_traverse(self):
        """
        Algorithm Inorder(tree)
        1. Traverse the left subtree, i.e., call Inorder(left-subtree)
        2. Visit the root.
        3. Traverse the right subtree, i.e., call Inorder(right-subtree)
        """
        res = []

        def inorder(node):
            if self.root is None:
                return
            if node:
                inorder(node.left)
                res.append(node.data)
                inorder(node.right)

        inorder(self.root)
        return res


def it_binary_search(arr, key):
    """
    Binary Search Algorithm: The basic steps to perform Binary Search are:
    Begin with the mid element of the whole array as a search key.
    If the value of the search key is equal to the item then return an index of the search key.
    Or if the value of the search key is less than the item in the middle of the interval,
    narrow the interval to the lower half. Otherwise, narrow it to the upper half.
    Repeatedly check from the second point until the value is found or the interval is empty.

    1. Assumes array is sorted
    2.
    return: point where key is found in arr
    """
    start = 0
    arr = sorted(arr)
    end = len(arr)
    while True:
        mid = start + end // 2
        if arr[mid] == key:
            return mid
        if key < arr[mid]:
            end = mid
        elif key > arr[mid]:
            start = mid
        else:
            return -1


def binary_search(arr, key):
    first_start = 0
    first_end = len(arr)
    first_mid = first_start + first_end // 2

    def rec_binary_search(start, end, mid, key, arr):
        if start > end:
            return -1
        if arr[mid] == key:
            return mid
        if key < arr[mid]:
            end = mid
            mid = start + end // 2
            return rec_binary_search(start, end, mid, key, arr)
        elif key > arr[mid]:
            start = mid
            mid = start + end // 2
            return rec_binary_search(start, end, mid, key, arr)

    return rec_binary_search(first_start, first_end, first_mid, key, arr)


if __name__ == '__main__':
    item = BinaryTree()
    # item.insert(1)
    # item.insert(2)
    # item.insert(3)
    item.it_insert(1)
    item.it_insert(2)
    item.it_insert(3)
    # item.traverOder()
    # print(item.root)
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 3))

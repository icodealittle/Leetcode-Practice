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

    '''
    def traverse(self):
        """
        1.1 Create an empty stack
        1 Do following while root is not NULL
        a) Push root's right child and then root to stack.
        b) Set root as root's left child.
        2 Pop an item from stack and set it as root.
        a) If the popped item has a right child and the right child
        is at top of stack, then remove the right child from stack,
        push the root back and set root as root's right child.
        b) Else print root's data and set root as NULL.
        3 Repeat steps 2.1 and 2.2 while stack is not empty.
        """
        copy = self.root
        stack = Stack() # Create an empty stack
        # Go all the way left until node.left is None
        while copy is not None: #  Do following while root is not NULL
            # Push root's right child and then root to stack.
            if copy.right is not None:
                stack.push(copy.right)
                stack.push(copy)
                # Set root as root's left child.
                copy = copy.left
                


            stack.push(copy)
            if copy.left is not None:
                copy = copy.left
            elif copy.left is None:
                if copy.right is not None:
                    copy = copy.right
                else:

        print(stack)
        '''

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

    def traverOder(self):
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


if __name__ == '__main__':
    item = BinaryTree()
    # item.insert(1)
    # item.insert(2)
    # item.insert(3)
    item.it_insert(1)
    item.it_insert(2)
    item.it_insert(3)
    #item.traverOder()
    # print(item.root)
    print(item.traverOder())

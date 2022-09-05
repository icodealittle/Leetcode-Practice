from generic_stackandqueue import Stack

class TreeNode:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None

    def traverse(self):
        pass
    def iterative_traverse(self):
        """
        Go all the way left until, node.left == null
        Uses a stack
        """
        pass


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

        while stop: # Check if we should go left of right
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

            #3
                #<1
            #<2     #<3
                        #<4

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






if __name__ == '__main__':
    s = Stack()
    item = BinaryTree()
    #item.insert(1)
    #item.insert(2)
    #item.insert(3)
    item.it_insert(1)
    item.it_insert(2)
    item.it_insert(3)
    print(item.root)

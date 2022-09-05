class TreeNode:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data


class BinaryTree:
    def __init__(self):
        self.root = None

    def traverse(self):
        copy = self.root
        lst = []
        stop = True
        while stop:
            if copy is not None:
                lst.append(copy.data)
            if copy.left is not None:
                lst.append(copy.left.data)
                copy = copy.left
            if copy.right is not None:
                lst.append(copy.right.data)
                copy = copy.left


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


    # def travers_re(seft):
        
    #     self.traverOder

    def traverOder(self):
        
        #left -> root -> right
        lst = []
        copy = self.root
        
        if copy is not None:
            lst = self.traverOder(copy.left)
            lst.append(copy.data)
            lst = lst + self.traverOder(copy.right)
        return lst

if __name__ == '__main__':
    item = BinaryTree()
    #item.insert(1)
    #item.insert(2)
    #item.insert(3)
    item.it_insert(1)
    item.it_insert(2)
    item.it_insert(3)
    print(item.root)
    print(item.traverOder())

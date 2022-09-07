"""
There is one root node in each Trie
Each node of a Trie represents a string and each edge represents a character.
Every node consists of hashmaps or an array of pointers, with each index
representing a character and a flag to indicate if any string ends at the current node.


"""


class TrieNode:
    def __init__(self):
        children = TrieNode[26]
        word_count = 0
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def charAt(self, char):
        char = char.lower()
        return ord(char) - ord('a')

    def insert(self, word):
        """
        Algorithm:

        Define a function insert(TrieNode *root, string &word) which will take two
        parameters one for the root and the other for the string that we want to insert in the Trie data structure.
        Now take another pointer currentNode and initialize it with the root node.

        Iterate over the length of the given string and check if the value is NULL or
        not in the array of pointers at the current character of the string.
        If It’s NULL then, make a new node and point the current character to this newly created node.
        Move the curr to the newly created node.
        Finally, increment the wordCount of the last currentNode, this implies that there is a string ending currentNode
        """
        current_node = self.root
        for char in word:
            index = self.charAt(char)
            # If they key you are looking for is not in the current nodes children list
            # Create a new TrieNode in that location to mark it
            if key not in current_node.children[index]:
                current_node.children[index] = TrieNode()
            # Move forward one
            current_node = current_node.children[index]
        current_node.isEndOfWord = True

    def starts_with(self):
        pass

    def search(self):
        pass

    def deletion(self):
        pass

if __name__ == '__main__':
    item = Trie()
    item.insert('hello')
    item.insert('happy')
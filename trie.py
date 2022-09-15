from ast import main


class Node:
    def __init__(self) -> None:
        self.children = dict()
        self.end = False

class Trie:
    def __init__(self) -> None:
        self.root = None
        
    def insert(self, word: str) -> None:
        word = word.lower()
        if self.root is None:
            self.root = Node()
        copy = self.root
        for char in word:
            if char not in copy.children:
                copy.children[char] = Node()
            copy = copy.children[char] 
        copy.end = True
    
    def search(self, word: str) -> bool:
        word = word.lower()
        if self.root is None:
            return False
        copy = self.root
        for char in word:
            if char not in copy.children:
                return False
            copy = copy.children[char]
        return copy.end
    
    def startWith(self, word: str) -> bool:
        word = word.lower()
        if self.root is None:
            return False
        copy = self.root
        for char in word:
            if char not in copy.children:
                return False
            copy = copy.children[char]
        return copy.end

if __name__ == '__main__':
    item = Trie()
    item.insert('cat')
    item.insert('dog')
    print(item.search('cat'))
    print(item.search('zebra'))
    print(item.startWith('c'))
    print(item.startWith('ca'))
    print(item.startWith('cat'))
    
          
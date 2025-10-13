class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        
        
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def insert_many(self, words: list[str])->None:
        for word in words:
           self.insert(word) 
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end
    
    def startwith(self, prefix:str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True   




trie = Trie()
trie = Trie()
trie.insert_many(["apple", "banana", "bat"])
print(trie.startwith("appl"))
print(trie.startwith('aapl'))
print(trie.search("apple"))    # True
print(trie.search("banana"))     # False

print(trie.search("bat"))      # True
print(trie.search("bad"))      # False

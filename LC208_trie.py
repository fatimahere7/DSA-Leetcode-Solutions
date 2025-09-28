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
trie.insert("apple")
trie.insert("app")
trie.insert("bat")
print(trie.startwith("appl"))
print(trie.startwith('aapl'))
print(trie.search("apple"))    # True
print(trie.search("appl"))     # False

print(trie.search("bat"))      # True
print(trie.search("bad"))      # False

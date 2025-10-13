

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()   
    
    def insert(self , word : str)->None:
        node = self.root
        for char in word:
            if char not in node.children:
               node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.word = word
    def insertMany(self , words:list[str])->None:
        for word in words:
            self.insert(word)        
    
    def startWith(self , prefix:str)->None:
        node = self.root
        if prefix not in node.children:
            return False
        return True

def wordSearch(board ,words : list[str])-> None:
    trie = Trie()
    trie.insertMany(words)
    res = []
    rows , cols = len(board), len(board[0])
    
    def dfs(board,i,j,node,res):
        char = board[i][j]
        curr = node.children[char]
        if curr.is_end:
            res.append(curr.word)
            curr.is_end = False
        
        
        board[i][j]="#"
        for x , y in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr , nc = i + x, j+y
            if 0<=nr<rows and 0<=nc<cols and board[nr][nc] in curr.children:
                dfs(board , nr , nc , curr, res )
        board[i][j] = char  #unmarked
         
    for r in range(rows):
        for c in range(cols):
            prefix = board[r][c]
            if trie.startWith(prefix):
                dfs(board,r , c , trie.root ,res)
    
    return list(res)
    
    
board = [
    ["o", "a", "a", "n"], 
    ["e", "t", "a", "e"], 
    ["i", "h", "k", "r"], 
    ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
board1 = [
    ['B', 'A', 'L', 'L'],
    ['A', 'T', 'A', 'E'],
    ['T', 'E', 'L', 'L']
]

words1 = ["BAT", "BALL", "TELL", "BATE"]

print(wordSearch(board, words))
print(wordSearch(board1 , words1))

                 
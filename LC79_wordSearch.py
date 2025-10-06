#Leetcode word search Lc # 79
def wordSearch(board , word):
    if not board:
        return False
    rows, cols = len(board), len(board[0])
    path = set()
    
    
    def dfs(r ,c ,i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or r >= rows or c >= cols or word[i] != board[r][c] or (r , c) in path):
            return False
        path.add((r ,c))
        res = (
            dfs(r+1 , c , i+1) or
            dfs(r-1 , c , i+1) or
            dfs(r , c+1 , i+1) or
            dfs(r , c-1 , i+1)             
        )
        path.remove((r ,c))
        return res
    for r in range(rows):
        for c in range(cols):
            if dfs(r , c , 0):
                return True 
    return False

board = [
         ["A", "B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]
        ]
word = "ABCCED"        

board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word1 = "SEE"
board2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word2 = "ABCB"
print(wordSearch(board, word))
print(wordSearch(board1 , word1))
print(wordSearch(board2, word2))

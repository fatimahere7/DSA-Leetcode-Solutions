from collections import deque


# DFS
def NoOfIslandsDFS(grid):
    if not grid:
        return 0
    islands = 0
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
            return

        grid[r][c] = '0'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c)
    return islands

# BFS


def NoOfIslandsBFS(grid):
    if not grid:
        return 0
    islands = 0
    rows, cols = len(grid), len(grid[0])

    def bfs(startRow, startCol):
        queue = deque()
        queue.append((startRow, startCol))
        grid[startRow][startCol] = "0"

        while queue:
            row, col = queue.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr , nc = row + dr , col + dc
                if (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1'):
                    queue.append((nr, nc))
                    grid[nr][nc] = '0'

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                bfs(r, c)
    return islands


grid1 = [
    ["1", "1", "0"],
    ["0", "1", "0"],
    ["1", "0", "1"]
]
grid11 = [
    ["1", "1", "0"],
    ["0", "1", "0"],
    ["1", "0", "1"]
]
grid2 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
grid22 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
grid3 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
grid33 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(f"DFS: {NoOfIslandsDFS(grid1)}")
print(f"BFS: {NoOfIslandsBFS(grid11)}")
print(f"DFS: {NoOfIslandsDFS(grid2)}")
print(f"BFS: {NoOfIslandsDFS(grid22)}")
print(f"DFS: {NoOfIslandsDFS(grid3)}")
print(f"BFS: {NoOfIslandsDFS(grid33)}")

grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

rows , cols = len(grid) , len(grid[0])
for r in range(rows):
    for c in range(cols):
        print(grid[r][c] , end=" ")
    print()    
        

def find_repeat(grid,expsum):
    seen = {}
    actualsum = 0
    for row in grid:
        for val in row:
            actualsum += val
            if val in seen:
                a = val
            seen[val] = True
    b = round(expsum + a - actualsum)
    # print(expsum)
    return {a,b}
            

grid = [[9, 1,7],[8,9,2],[3,4,6]]
# grid = [[1, 2], [2, 3]]
n = len(grid)
expected_sum = (n*n)*((n*n)+1)/2
print(find_repeat(grid,expected_sum))    
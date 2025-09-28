def zigzagPattern(s:str,nRows:int) -> str:
    if nRows == 1 or nRows >= len(s):
        return s
    rows = [""]*nRows
    curr_row = 0
    going_down = False
    
    for char in s:
        rows[curr_row] += char
        if curr_row == 0 or curr_row == nRows-1:
            going_down = not going_down
        curr_row += 1 if going_down else -1
        
    return "".join(rows) 


s = "PAYPALISHIRING"
numRows = 3
print(zigzagPattern(s, numRows))

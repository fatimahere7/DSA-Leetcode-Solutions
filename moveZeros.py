arr = [0, 1, 0, 3, 12]

# Pointer for the position of next non-zero element
pos = 0
for i in range(len(arr)):
    if arr[i] != 0:
        arr[pos] , arr[i] = arr[i] , arr[pos]
        pos +=1
        
print(arr)        
        
        
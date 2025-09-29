def solution(nums):
    hashmap = {0:-1}
    sum = 0
    maxlen = 0
    for i , val in enumerate(nums):
        sum += 1 if val == 1 else -1
        
        if sum in hashmap:
            length = i - hashmap[sum]
            if length > maxlen:
                maxlen = length
                start = hashmap[sum] + 1
                end = i
        else:
            hashmap[sum] = i
    return maxlen , (start , end)                
            
            
arr = [0, 1, 0, 1, 1, 1, 0]
length, (s, e) = solution(arr)
print("Length:", length)        # 4
print("Indices:", (s, e))       # (0, 3)
print("Subarray:", arr[s:e+1])  # [0, 1, 0, 1]
print('\n')
arr = [0,0,1,1,1,0,0,1,0,0]
length, (s, e) = solution(arr)
print("Length:", length)        # 8
print("Indices:", (s, e))       # (0, 7)
print("Subarray:", arr[s:e+1])  # [0, 0, 1, 1, 1, 0, 0, 1]

# map = {}
# for i in range(len(arr)):
#     if arr[i] in map:
#         print(arr[i])
#     map[arr[i]]= True
def longest_substring(arr):
    
    for i in range(len(arr)):
        start = 0
        end = 0
        max_len = 0
        map = {}
        while end < len(arr):
            if arr[end] not in map:
                map[arr[end]]= end
                end += 1
                max_len = max(max_len, len(map))
            else:
                map.pop(start)     
                start += 1
        print("Max lenghth is :"+ max_len)        
        



string = "abcdabda"
longest_substring(string)        
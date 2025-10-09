# brute force O(n^2)
def two_sum1(array, target):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                return {i, j}


# better appraoch O(n log n) 
def two_sum2(array, target):
    arr_sorted= sorted(array)
    end = len(arr_sorted)-1
    start = 0
    while start < end:
       if arr_sorted[start] + arr_sorted[end] > target:
           end-=1
       elif arr_sorted[start] + arr_sorted[end] < target:
           start+=1
       elif arr_sorted[start] + arr_sorted[end] == target:
           return {start ,end}       

# optimized approach O(n)
def two_sum3(array , target):
    unorder_map = {}
    for i in range(len(array)):
        first = array[i]
        comp = target - first
        if comp in unorder_map:
            return {unorder_map[comp],i}
        unorder_map[array[i]] = i      

arr = [3, 1, 4, 6, 8]
target = 10
# target=9
# arr = [2, 7, 11, 5, 15]
print(two_sum1(arr, target))  # brute force
print(two_sum2(arr, target))  #2 pointer approach 
print(two_sum3(arr, target))  #hash map 

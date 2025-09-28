
# def recursiveSearch(arr, target st,end):
#     st = 0
#     end = len(arr)-1
#     while (st <= end):
#         # mid = (st+end)//2
#         mid = st + (end-st)//2  # opptimize
#         if target > arr[mid]:
#             return recursiveSearch(arr , target,mid+1,end)
#         elif target < arr[mid]:
#             return recursiveSearch(arr, target, st, mid-1)
#         else:
#             return mid

#     return -1



# itterative approach
def binarySearch(arr , target):
    st = 0 
    end = len(arr)-1
    while(st <= end):
        # mid = (st+end)//2
        mid = st + (end-st)//2  #opptimize
        if target > arr[mid]:
            st = mid+1
        elif target < arr[mid]:
            end = mid - 1
        else:
            return mid          
        
    return -1    




nums = [-1,0,3,5,9,12]
target = 9
print(binarySearch(nums , target))
nums = [-1, 0,3,5,9,12]
target = 2
print(binarySearch(nums, target))

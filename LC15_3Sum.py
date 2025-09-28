# Two pointer
def threeSum(nums):
    nums.sort()
    n = len(nums)
    result = [] 
    for i in range(n):
        if i>0 and nums[i] == nums[i-1]:
            continue
        tar = -nums[i]
        left, right = i+1 , n-1
        while left < right:
            sum = nums[left] + nums[right]
            if sum == tar:
                result.append([nums[i],nums[left] ,nums[right]])
                left +=1
                right -=1
                while left < right and nums[left] == nums[left-1]:
                    left+=1
                while left < right and nums[right] == nums[right+1]:
                    right -=1    
                       
            elif sum < tar:
                left +=1
            else:
                right -=1        
    return result    
 
# Hashmap
# def threeSum_hash(nums):
#     n = len(nums)
#     result = set()

#     for i in range(n):
#         seen = set()
#         target = -nums[i]
#         for j in range(i+1, n):
#             needed = target - nums[j]
#             if needed in seen:
#                 triplet = tuple(sorted([nums[i], nums[j], needed]))
#                 result.add(triplet)
#             seen.add(nums[j])

#     return list(result)
 
             
arr = [-1, 0, 1, 2, -1, -4]
print(threeSum(arr))

# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a subarray whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.
# Example 1:  Input: target = 7, nums = [2, 3, 1, 2, 4, 3] Output: 2
# Explanation: The subarray[4, 3] has the minimal length under the problem constraint.
# Example 2: Input: target = 4, nums = [1, 4, 4] Output: 1
# Example 3: Input: target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1] Output: 0


def minSubArrayLen(nums, target ):
    n = len(nums)
    curr_sum = 0
    min_length = float('inf')
    left=0
    
    
    for right in range(n):
        curr_sum += nums[right]
        while curr_sum >= target:
            min_length = min(min_length, right - left + 1)
            curr_sum -= nums[left]
            left += 1
            
    return min_length if min_length != float('inf') else 0


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(minSubArrayLen(nums , target))
print(minSubArrayLen([1, 1, 1, 1, 1, 1, 1, 1] , 11))
print(minSubArrayLen([1, 4, 4], 4))
#   O(n) T and O(1) spacce
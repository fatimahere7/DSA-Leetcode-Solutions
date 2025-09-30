def seachInRotatedArray(nums, target):
    start = 0
    end = len(nums)-1

    while start <= end:
        mid = start + (end-start)//2
        if nums[mid] == target:
            return mid

        if nums[start] <= nums[mid]:
            if nums[start] <= target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if nums[mid] < target <= nums[end]:
                start = mid + 1
            else:
                end = mid - 1
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(seachInRotatedArray(nums, target))  # Expected: 4

nums1 = [4, 5, 6, 7, 0, 1, 2]
target1 = 3
print(seachInRotatedArray(nums1, target1))  # Expected: -1

nums2 = [15, 18, 2, 3, 6, 12]
target2 = 3
print(seachInRotatedArray(nums2, target2))  # Expected: 3

def searchRange(nums , tar):
    def firstSearch(nums , tar):
        left , right = 0 , len(nums)-1
        first = -1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] >= tar:
                right= mid - 1
            else:
                left = mid + 1
            if nums[mid] == tar:
                first = mid
        return first           
                    
                   
    def lastSearch(nums, tar):
        left, right = 0, len(nums)-1
        last = -1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] <= tar:
                left = mid + 1
            else:
                right = mid - 1
            if nums[mid] == tar:
                last = mid
        return last
    
    return [firstSearch(nums, tar), lastSearch(nums, tar)]


print(searchRange([5, 7, 7, 8, 8, 10], 8))  # [3,4]
print(searchRange([5, 7,7,8,8,10], 6))  # [-1,-1]
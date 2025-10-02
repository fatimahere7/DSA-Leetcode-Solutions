#  Brute force
def subArrayEqKBF(nums , tar):
    start = 0
    
    count = 0
    for i in range(len(nums)):
        sum = 0
        for j in range(i ,len(nums)):
            sum += nums[j]
            if sum == tar:
                count+=1
           
            
    return count

#prefix sum
def subArrayEqkPS(nums, k):
    count = 0
    prefixSum = 0
    hashmap = {0:1}  #{prefixSum:frequency}
    for i in range(len(nums)):
        prefixSum += nums[i]
        if (prefixSum - k) in hashmap:
            count += hashmap[prefixSum-k]
        
        if prefixSum in hashmap:
                hashmap[prefixSum] += 1
        else:
            hashmap[prefixSum] = 1  
    return count                  
            


print(subArrayEqKBF([1,9,4,20,3,10,5] , 33)) 
print(subArrayEqkPS([1, 9,4,20,3,10,5] , 33)) 
print(subArrayEqkPS([1, -1, 1, -1, 1], 0))

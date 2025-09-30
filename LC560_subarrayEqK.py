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

print(subArrayEqKBF([1,9,4,20,3,10,5] , 33)) 
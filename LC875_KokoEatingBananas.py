from typing import List
def kokoEatingSpeed(piles: List[int], h: int)->int:
    def hoursNeed(k:int)->int:
        sum = 0
        for pile in piles:
            sum += (pile + k -1)//k
        return sum    
        
    low , high = 1 , max(piles)
    while low < high:
        mid = (low + high)//2
        if hoursNeed(mid) <= h:
            high = mid
        else:
            low = mid + 1
    return low            


print(kokoEatingSpeed([3, 6, 7, 11], 8))  #4
print(kokoEatingSpeed([30, 11, 23, 4, 20], 5)) #30

print(kokoEatingSpeed([30, 11, 23, 4, 20], 6)) #23

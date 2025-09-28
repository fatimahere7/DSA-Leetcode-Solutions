class solution(object):
    def squareSum(self , n):
        sum = 0
        while n > 0:
           digit = n % 10
           sum += digit * digit
           n = n//10
        return sum
    
    def isHappy(self ,n):
        slow = n
        fast = self.squareSum(n)
        
        while slow != fast and fast !=  1:
            slow = self.squareSum(slow)
            fast = self.squareSum(self.squareSum(fast))
        
        return fast == 1

sol = solution()     
print(sol.isHappy(19))   #  True (19 is a happy number)
print(sol.isHappy(20))   # false
print(sol.isHappy(2))    # Expected False (2 is not happy)
print(sol.isHappy(7))    # Expected True (7 is happy)
print(sol.isHappy(4))    # Expected False (4 enters a cycle)
print(sol.isHappy(1))    # Expected Tru

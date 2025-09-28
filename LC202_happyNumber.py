class solution(object):
    def squareSum(n):
        
        while n > 0:
           digit1 = (n//10)*(n//10)
           digit2 = (n%10)*(n%10)
           sum = digit1 + digit2
        return sum
        
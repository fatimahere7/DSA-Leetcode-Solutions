
# def toBinary(num):
#     if num == 0:
#         return '0'
#     bits = ""
#     while num > 0:
#         bits = str(num % 2) + bits
#         num //= 2
#     return bits


# print(toBinary(9))
def myPow(x, n):
    if n ==0:
        return 1.0
    if x == 0:
        return 0.0
    if x == 1:
        return 1.0
    if x == -1 & n%2 == 0:
        return 0.0
    if x == -1 & n % 2 != 0:
        return -1.0
    ans = 1.0
    if n < 0:
        x = 1/x
        n = -n
    while n > 0:
        bit = n % 2
        if bit != 0:
            ans *= x

        x *= x
        n //= 2
    return ans


print(myPow(2, 10))

print(myPow(2.5, 10))
print(myPow(3,-7))

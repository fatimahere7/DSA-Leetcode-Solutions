
# factorial
def fact(n: int) -> int:
    if n == 1:
        return 1
    return n * fact(n-1)


def sum(n: int) -> int:
    if n == 0:
        return 0
    return n + sum(n-1)


def print_increasing(n):
    if n == 0:
        return
    print(n)
    print_increasing(n-1)
    print(n)


def reversestring(s: str) -> None:
    if len(s) <= 1:
        return s
    return reversestring(s[1:]) + s[0]


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


print(fact(5))
print(sum(5))
print_increasing(5)
print(reversestring("hello"))
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False

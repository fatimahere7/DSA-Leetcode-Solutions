# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.


# Example 1: Input: s = "()"  Output: true
# Example 2: Input: s = "()[]{}"  Output: true
# Example 3: Input: s = "(]"  Output: false
# Example 4:  Input: s = "([])" Output: true
# Example 5:  Input: s = "([)]"  Output: false

def isValid(s: str) -> bool:
    stack = []
    openToClose = {')':'(',']':'[','}':'{'}
    
    for char in s:
        if char in openToClose:
            top = stack.pop() if stack else '#'
            if openToClose[char] != top:
                return False
        else:
            stack.append(char)
        
    return True if not stack else False        




print(isValid("()"))         #True
print(isValid('()[]{}'))     #True
print(isValid("(]"))         #False
print(isValid("([)]"))       #False
print(isValid("{[]}"))       

                

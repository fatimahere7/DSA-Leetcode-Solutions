def plandromeStr(s:str) ->str:
    if len(s) < 2:
        return s
    res = ""
    maxLen = 0
    for i in range(len(s)):
        
        left , right = i , i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > maxLen:
                res = s[left:right+1]
                maxLen = right - left + 1
            left-=1
            right+=1
            
        left, right = i, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > maxLen:
                res = s[left:right+1]
                maxLen = right - left + 1
            left -= 1
            right += 1
            
    return res        


# Test cases
print(plandromeStr("babad"))  # "bab" or "aba"
print(plandromeStr("cbbd"))   # "bb"
print(plandromeStr("a"))      # "a"
print(plandromeStr("ac"))

# Given a string s, find the length of the longest substring without duplicate characters.


# Example 1:  Input: s = "abcabcbb"  Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2: Input: s = "bbbbb"  Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3: Input: s = "pwwkew"
# Output: 3: Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.



#sliding window
def longestSubstring(s:str)->str:
    l = 0
    set_map = set()
    max_len = 0
    for r in range(len(s)):
        while s[r] in set_map:
            set_map.remove(s[l])
            l += 1
        set_map.add(s[r])    
        max_len = max(max_len, r-l+1)
    
    return max_len    

# gonna solve with hash map in future

        
    
print(longestSubstring("pwwkew"))
print(longestSubstring("bbbbbb"))
print(longestSubstring("abcadfsa"))

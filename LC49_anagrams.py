# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.
# Example 1: Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
# Explanation:  There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2: Input: strs = [""]  Output: [[""]]
# Example 3: Input: strs = ["a"] Output: [["a"]]



from collections import defaultdict
# by sorting klogk 
def groupAnagrams_Sorting(strs):
    group = defaultdict(list)
    for word in strs:
        key = "".join(sorted(word))
        group[key].append(word)
        
    return list(group.values())   


# O(m.n)
def groupAnagrams_count(strs):
    group = defaultdict(list)

    for word in strs:
        count = [0]*26
        for char in word:
            count[ord(char)-ord('a')] +=1
        group[tuple(count)].append(word)
    return list(group.values())        
        # in dict [1,0,0,0,1,0,0,0,.....1,0,0.. : eat ,tea]

    
print(groupAnagrams_Sorting(["eat", "tea","tan","ate","nat","bat"]))    
print(groupAnagrams_count(["eat", "tea", "tan","ate","nat","bat"])) 
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
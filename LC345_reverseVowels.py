def is_vowel(ch: str) -> bool:
    return ch.lower() in "aeiou"
def reverseVowel(s:str)->str:
    l = 0
    r = len(s)-1
    s = list(s)

    while l < r:
        while l < r and not is_vowel(s[l]):
            l +=1 
        while l < r and not is_vowel(s[r]):
            r-=1
        
        s[l] , s[r] = s[r] , s[l]   
        l+=1
        r-=1    
    return "".join(s)   
                

print(reverseVowel("IceCreAm"))
print(reverseVowel("hello"))
    
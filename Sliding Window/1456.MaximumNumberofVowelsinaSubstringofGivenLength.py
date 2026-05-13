class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        max_v = 0
        current_vowels = 0
        
        vowels = {'a','e','i','o','u'}
        
        for right in range(len(s)):
            
            if s[right] in vowels:
                current_vowels +=1
            
            if right >=k:
                if s[right-k] in vowels:
                    current_vowels -=1            
            max_v = max(max_v,current_vowels)
            
            if max_v == k:
                return k
        return max_v
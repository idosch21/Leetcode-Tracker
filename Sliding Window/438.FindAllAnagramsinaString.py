class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []
        
        result = []
        
        freq_p = [0]*26
        freq_s = [0]*26
        
        for letter in p:
            freq_p[(ord(letter)-ord('a'))] +=1
            
        for right in range(len(s)):
            
            freq_s[(ord(s[right])-ord('a'))]+=1
            
            if right >=len(p):
                freq_s[(ord(s[right-len(p)])-ord('a')))]-=1
            
            if freq_s == freq_p:
                result.append(right-len(p)+1)
        return result
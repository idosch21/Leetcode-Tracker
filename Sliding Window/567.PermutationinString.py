class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1_map = [0]*26
        freq_map = [0]*26  
        window = len(s1)
        
        for i in range(window):
            s1_map[ord(s1[i])-ord('a')] += 1
            freq_map[ord(s2[i])-ord('a')] += 1
        
        if s1_map == freq_map:
            return True
        
        for i in range(window,len(s2)):
            freq_map[ord(s2[i-window])-ord('a')] -= 1 #remove the i-window char
            freq_map[ord(s2[i])-ord('a')] += 1 #add the i-th char
            
            if freq_map == s1_map:
                return True
        return False
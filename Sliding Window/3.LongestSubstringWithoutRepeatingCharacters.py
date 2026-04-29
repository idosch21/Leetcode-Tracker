class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        
        left = 0
        max_len = 0
        seen = {}
        for right in range(len(s)):
            
            if s[right] in seen and seen[s[right]] >= left:
                #if s[right] is in our map, it means we saw it in our window
                #and if its also bigger than left
                #its in our window then weneed to shrink the window
                left = seen[s[right]] +1
            seen[s[right]] = right
            #we put s[right] in the seen map and its index
            max_len = max(max_len,right-left+1)
        
        return max_len
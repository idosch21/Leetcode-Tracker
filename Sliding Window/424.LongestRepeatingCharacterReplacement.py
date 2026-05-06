class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        max_f = 0
        result = 0
        
        array = [0]*26
        
        for right in range(len(s)):
            
            index = ord(s[right]) - ord('A')
            array[index] +=1
            max_f = max(max_f,array[index])
            
            window_len = (right-left+1)
            
            if window_len - max_f > k:
                array[left] -=1
                left+=1
            else:
                result = window_len
        
        return result
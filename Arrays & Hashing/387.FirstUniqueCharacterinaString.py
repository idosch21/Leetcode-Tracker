class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Count frequency of each character
        counter = collections.Counter(s)
        
        # Find first character with frequency 1
        for index, letter in enumerate(s):
            if counter[letter] == 1:
                return index
        
        return -1

# TRICK: Count all characters, then iterate to find first with count = 1.
# T(N) = O(n)
# S(N) = O(k) where k = alphabet size
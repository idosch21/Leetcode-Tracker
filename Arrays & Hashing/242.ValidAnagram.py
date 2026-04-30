class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Quick check: different lengths can't be anagrams
        if len(s) != len(t):
            return False
        
        # Count character frequencies for both strings
        freq_s = collections.Counter(s)
        freq_t = collections.Counter(t)
        
        # Anagrams have identical character counts
        return freq_s == freq_t

# TRICK: Compare character frequency counts. Use Counter or array
# for 26 letters. Equal counts = anagrams.
# T(N) = O(n)
# S(N) = O(1) or O(k) where k = alphabet size
    
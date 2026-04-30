class Solution:
    def firstUniqChar(self, s: str) -> int:

        counter = collections.Counter(s)
        
        for index, letter in enumerate(s):
            if counter[letter]==1:
                return index
        return -1
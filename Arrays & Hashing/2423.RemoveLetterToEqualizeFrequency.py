class Solution:
    def equalFrequency(self, word: str) -> bool:

        counts = collections.Counter(word)
        
        for char in counts:
            
            counts[char] -=1 
            
            my_set = set(counts.values())
            
            if 0 in my_set:
                my_set.remove(0)
            if len(my_set) ==1:
                return True
            counts[char] += 1
        return False
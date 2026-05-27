class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        my_map = defaultdict(list)
        result = 0
        
        for index,letter in enumerate(word):
            my_map[letter].append(index)
            
        for letter in my_map:
            
            if not letter.islower():
                continue
            
            upper = letter.upper()
            if upper in my_map:
                if max(my_map[letter]) < min(my_map(upper)):
                    result += 1
        return result
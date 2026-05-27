class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        last_lower = {}
        first_upper = {}
        result = 0
        
        for i , letter in enumerate(word):
            if letter.islower():
                last_lower[letter] = i
            else:
                if letter not in first_upper:
                    first_upper[letter] = i
        
            
            
        for letter in last_lower:
            
            if letter.upper() in first_upper:
                upper_letter = letter.upper()
                if last_lower[letter] < first_upper[upper_letter]:
                    result += 1
        return result
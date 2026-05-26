class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        array_smaller = [0]*26
        array_larger = [0]*26
        
        for letter in word:
            if letter.isupper():
                array_larger[ord(letter)-ord('A')] += 1
            else:
                array_smaller[ord(letter)-ord('a')] += 1
        
        counter = 0
        
        for i in range(26):
            if array_larger[i] >=1 and array_smaller[i] >= 1:
                counter +=1
        
        return counter
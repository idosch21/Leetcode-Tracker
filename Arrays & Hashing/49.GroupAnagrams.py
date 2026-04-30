class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Hash map: key = character frequency tuple, value = list of anagrams
        # Using tuple as key because lists are not hashable (mutable)
        my_dict = defaultdict(list)
        
        for word in strs:
            # Create a frequency count array for 26 lowercase letters
            # This serves as the "signature" for an anagram group
            char_freq = [0] * 26
            
            # Count each character in the current word
            for letter in word:
                # Convert letter to index: 'a' -> 0, 'b' -> 1, etc.
                char_freq[ord(letter) - ord('a')] += 1
            
            # Use tuple(char_freq) as key - tuples are immutable and hashable
            # Anagrams will have the same character frequency signature
            my_dict[tuple(char_freq)].append(word)
        
        # Return all anagram groups as a list of lists
        return list(my_dict.values())

# T(n) = O(n * k) - n words, each processing up to k characters
# S(n) = O(n * k) - storing all strings in the hash map
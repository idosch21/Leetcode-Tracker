class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Count frequency of each character in the word
        counts = collections.Counter(word)
        
        # Try removing each character one at a time
        for char in counts:
            # Temporarily remove one occurrence of current character
            counts[char] -= 1
            
            # Get all non-zero frequency values
            my_set = set(counts.values())
            
            # Remove 0 from set (character we just removed completely)
            if 0 in my_set:
                my_set.remove(0)
            
            # If all remaining characters have the same frequency, return True
            # This means removing one letter makes all frequencies equal
            if len(my_set) == 1:
                return True
            
            # Restore the character count for next iteration
            counts[char] += 1
        
        # No single removal could equalize frequencies
        return False

# TRICK: Try removing each character and check if remaining frequencies can be equal.
# Use set to check if all non-zero frequencies are the same.
# T(N) = O(n * k) where k = unique characters
# S(N) = O(k)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Handle empty string edge case
        if not s:
            return 0
        
        # Left pointer of sliding window
        left = 0
        # Track maximum length found
        max_len = 0
        # Dictionary: character -> most recent index
        seen = {}
        
        # Right pointer expands the window
        for right in range(len(s)):
            # If current character was seen and is within current window
            if s[right] in seen and seen[s[right]] >= left:
                # Character is a duplicate within window
                # Move left pointer to just after previous occurrence
                left = seen[s[right]] + 1
            
            # Update character's most recent index
            seen[s[right]] = right
            
            # Calculate current window length and update max
            max_len = max(max_len, right - left + 1)
        
        return max_len

# TRICK: Sliding window with hash map. Expand right, shrink left when
# duplicate found. Store last seen index of each character.
# T(N) = O(n)
# S(N) = O(min(m)) where m = alphabet size
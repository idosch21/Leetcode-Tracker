class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointers from both ends
        left = 0
        right = len(s) - 1
        
        # Move towards center
        while left <= right:
            # Skip non-alphanumeric characters from left
            # Continue until we find a valid character or cross right
            while not s[left].isalnum() and left < right:
                left += 1
                continue
            
            # Skip non-alphanumeric characters from right
            while not s[right].isalnum() and left < right:
                right -= 1
                continue
            
            # Compare characters (case-insensitive)
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                # Characters don't match - not a palindrome
                return False
        
        # All characters matched - it's a palindrome
        return True

# TRICK: Two pointers from ends. Skip non-alphanumeric, compare
# case-insensitive. Move inward until meeting or mismatch.
# T(N) = O(n)
# S(N) = O(1)
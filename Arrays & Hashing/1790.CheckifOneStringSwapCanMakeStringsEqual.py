class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # If strings are already equal, no swap needed - return True
        if s1 == s2:
            return True
        
        # List to store indices where s1 and s2 differ
        diff = []
        size = len(s1)
        
        # Iterate through both strings simultaneously
        for i in range(size):
            # Check if characters at current position differ
            if s1[i] != s2[i]:
                # Record the position of difference
                diff.append(i)
                # Early exit: more than 2 differences cannot be fixed with one swap
                if len(diff) > 2:
                    return False
        
        # Valid swap requires exactly 2 differing positions
        if len(diff) == 2:
            i, j = diff[0], diff[1]
            # Check if swapping positions i and j in s1 equals s2
            # After swap: s1[i] should equal s2[j] AND s1[j] should equal s2[i]
            return s1[i] == s2[j] and s1[j] == s2[i]
        
        # Either 0 or 1 differences - cannot be fixed with one swap
        return False

# TRICK: Find all differing positions. If exactly 2, check if swapping
# them makes strings equal. More than 2 differences = impossible.
# T(N) = O(n)
# S(N) = O(1)
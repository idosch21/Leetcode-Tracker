class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        my_stack = []
        # Map: opening bracket -> corresponding closing bracket
        mapper = {"{": "}", "(": ")", "[": "]"}
        # Set of opening brackets for quick lookup
        closer = {"[", "(", "{"}

        # Edge case: odd length string can't be valid
        if len(s) % 2 != 0:
            return False

        # Edge case: first character must be opening bracket
        if s[0] not in closer:
            return False
        
        # Process each character
        for char in s:
            if char in closer:
                # Opening bracket - push to stack
                my_stack.append(char)
            else:
                # Closing bracket - must match most recent opening
                if my_stack:
                    # Pop and check if it matches
                    closer_char = my_stack.pop()
                    if char != mapper[closer_char]:
                        return False
                else:
                    return False
        
        # Valid if stack is empty (all brackets matched)
        return False if my_stack else True

# TRICK: Stack-based matching. Push opening brackets, pop and verify
# when closing bracket encountered. At end, stack must be empty.
# T(N) = O(n)
# S(N) = O(n)
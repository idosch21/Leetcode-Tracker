class Solution:
    def removeDuplicates(self, s: str) -> str:
        # Handle empty string edge case
        if not s:
            return ""
        
        # Stack to keep track of characters
        stack = []
        
        # Process each character in string
        for char in s:
            # If stack has character and it matches current character
            # They are adjacent duplicates - remove the stack top
            if stack and char == stack[-1]:
                stack.pop()
            else:
                # Either stack is empty or characters don't match
                # Add current character to stack
                stack.append(char)
        
        # Join stack characters to form result
        return "".join(stack)

# TRICK: Stack-based removal. When current char matches stack top,
# they form adjacent pair - pop to remove. Otherwise push.
# Continue until no adjacent duplicates remain.
# T(N) = O(n)
# S(N) = O(n)
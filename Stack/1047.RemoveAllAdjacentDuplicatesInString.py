class Solution:
    def removeDuplicates(self, s: str) -> str:

        if not s:
            return ""
        
        stack = []
        
        for char in s:##for every letter in s, we will first check if there is a letter in the stack
            #if so we will check if the last letter in the stack is equal to our current letter
            #if so we know that they are adjacent and we need to remove the letter in the stack
            #thats why we pop.
            if stack and char == stack[-1]:
                stack.pop()
            else:##if not, either the stack is empty or the two letters are not duplicates so we can append
                stack.append()
        
        return "".join(stack)
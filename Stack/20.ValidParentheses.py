class Solution:
    def isValid(self, s: str) -> bool:
        my_stack = []
        mapper = {"{":"}", "(":")","[":"]"}
        closer = {"[","(","{"}

        #edge case:
        if len(s) %2 != 0:
            return False

        if s[0] not in closer:
            return False
        
        for char in s:
            if char in closer:
                my_stack.append(char)
            else:
                if my_stack:
                    closer_char = my_stack.pop()
                    if char != mapper[closer_char]:
                        return False

        return False if my_stack else True
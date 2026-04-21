class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {"+","-","/","*"}
        #each time i can only do operands on 2 values,
        #so ill get a stack with my values,
        #if the string is not operand then ill append it to the stack
        #if its operand ill pop what i have in the stack and do the math?
        stack = []
        result = 0

        for char in tokens:
            if char not in operands:
                stack.append(int(char))
            else:
                #char is operand so we need to pop twice and then apply the operand.
                first_val = int(stack.pop())
                second_val = int(stack.pop())
                if char == "+":
                    stack.append(first_val+second_val)
                elif char == "-":
                    stack.append(second_val-first_val)
                elif char == "*":
                    stack.append(first_val*second_val)
                else:
                    stack.append(second_val/first_val)
                print(stack)
        return int(stack[0])


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Set of operators for quick lookup
        operands = {"+", "-", "/", "*"}
        
        # Stack to hold numbers (operands)
        stack = []
        
        # Process each token
        for char in tokens:
            if char not in operands:
                # Token is a number - push to stack
                stack.append(int(char))
            else:
                # Token is an operator - pop two values
                # Note: first pop is second operand, second pop is first operand
                # (order matters for subtraction and division)
                first_val = int(stack.pop())
                second_val = int(stack.pop())
                
                # Apply operator and push result back to stack
                if char == "+":
                    stack.append(second_val + first_val)
                elif char == "-":
                    stack.append(second_val - first_val)
                elif char == "*":
                    stack.append(first_val * second_val)
                else:
                    # Division: truncate towards zero
                    stack.append(int(second_val / first_val))
        
        # Final result is the only item left in stack
        return int(stack[0])

# TRICK: Stack-based evaluation. Push numbers, pop two for operator,
# apply to second popped as first operand. Result back on stack.
# T(N) = O(n)
# S(N) = O(n)


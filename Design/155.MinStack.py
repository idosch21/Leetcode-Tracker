class MinStack:
    def __init__(self):
        # Main stack to store all elements
        self.stack = []
        # Auxiliary stack to track minimum values
        # Each entry corresponds to min at that stack depth
        self.minStack = []

    def push(self, val: int) -> None:
        # Push value to main stack
        self.stack.append(val)
        
        # Calculate new minimum: min of current value and previous min
        # If minStack is empty, val is the minimum
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        # Pop from both stacks (they stay in sync)
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return top element of main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return top of minStack (current minimum)
        return self.minStack[-1]

# TRICK: Two stacks - main for values, aux for minimums at each level.
# When pushing, calculate new min and push to aux stack.
# When popping, pop from both. O(1) for all operations.
# T(N) = O(1) for all operations
# S(N) = O(n)
        

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Climbing Stairs: Calculate the number of distinct ways to reach the top of a staircase with n steps.
        
        TRICK USED:
        - Dynamic Programming (Bottom-Up): Recognizing that the problem is a variation of the Fibonacci sequence.
        - Space Optimization: Instead of an array of size n, we only maintain the two previous values needed to compute the current state.
        
        WHY IT WORKS:
        - To reach step i, you can only come from step i-1 (by taking 1 step) or step i-2 (by taking 2 steps).
        - Therefore, the recurrence relation is: f(i) = f(i-1) + f(i-2).
        - By starting from the base cases (1 way for step 1, 2 ways for step 2), we can iteratively build up to n.
        """
        
        # Base cases: for 1 step, there's 1 way; for 2 steps, there are 2 ways
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize the two previous steps (representing ways to reach step i-1 and i-2)
        one_step_back = 2
        two_steps_back = 1
        
        # Iteratively calculate ways for each step from 3 up to n
        for i in range(3, n + 1):
            # The current number of ways is the sum of the previous two steps
            current = two_steps_back + one_step_back
            
            # Update pointers for the next iteration
            two_steps_back = one_step_back
            one_step_back = current
            
        return one_step_back

# COMPLEXITY ANALYSIS:
# T(n) = O(n) - Time Complexity
#   - We loop from 3 to n exactly once, performing constant-time additions and updates.
#
# S(n) = O(1) - Space Complexity
#   - We only store a fixed number of integer variables regardless of the input size n.
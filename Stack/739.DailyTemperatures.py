class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Result array initialized to 0 (no warmer day found)
        size = len(temperatures)
        result = [0] * size
        
        # Stack stores (temperature, index) pairs
        # Keeps track of days waiting for warmer temperature
        stack = []
        
        # Iterate through each day
        for i, t in enumerate(temperatures):
            # While current day is warmer than the day at stack top
            # Pop and calculate days until warmer weather
            while stack and t > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                # Days until warmer = current index - popped index
                result[stackInd] = i - stackInd
            
            # Push current day to stack (waiting for warmer day)
            stack.append((t, i))
        
        # Days that never found warmer weather stay 0
        return result

# TRICK: Monotonic decreasing stack. Push indices waiting for warmer day.
# When warmer day found, pop and calculate distance. Process in single pass.
# T(N) = O(n) - each element pushed and popped at most once
# S(N) = O(n)



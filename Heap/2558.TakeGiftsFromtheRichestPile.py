import heapq
import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        """
        Take Gifts From the Richest Pile: Reduce the total number of gifts by repeatedly taking the square root of the largest pile.
        
        TRICK USED:
        - Max-Heap Simulation: Since Python's heapq module only provides a min-heap, we negate all gift counts.
        - This allows the largest positive values to act as the smallest negative values, effectively giving us O(log n) access to the maximum.
        - Math.isqrt: Using an integer-specific square root function to efficiently handle the floor value requirement.
        
        WHY IT WORKS:
        - To reduce the total sum as much as possible, we must greedily target the largest available pile in every step.
        - A heap allows us to find and update the maximum element in logarithmic time, which is necessary when k is large.
        - After k operations, the sum of the remaining values gives the final answer.
        """
        # Convert the list into a max-heap by negating all values
        # Python's heapq is a min-heap, so negation allows us to simulate max-heap behavior
        for i in range(len(gifts)):
            gifts[i] *= -1
        
        # Transform the negated list into a heap structure in-place
        heapq.heapify(gifts)
        
        # Perform the gift-taking operation k times
        for i in range(k):
            # Extract the current maximum (represented by the most negative value)
            max_val = -heapq.heappop(gifts)
            
            # Take the floor of the square root and push it back as a negative value
            heapq.heappush(gifts, -math.isqrt(max_val))
        
        # Sum the negative values and negate the result to get the final positive total
        return -sum(gifts)

# COMPLEXITY ANALYSIS:
# T(n) = O(n + k log n) - Time Complexity
#   - Negating the list and heapify both take O(n) time.
#   - We perform k iterations of pop and push, each taking O(log n) time.
#
# S(n) = O(n) - Space Complexity
#   - We modify the input list to create the heap, which occupies O(n) space.
#   - No additional data structures are used, resulting in O(1) auxiliary space beyond the input.
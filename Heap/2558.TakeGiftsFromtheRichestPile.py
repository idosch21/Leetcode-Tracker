class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Convert to max heap by negating all values
        # Python heapq is a min heap, so we negate to simulate max heap
        for i in range(len(gifts)):
            gifts[i] *= -1
        
        # Convert list to heap (min heap of negative values = max heap)
        heapq.heapify(gifts)
        
        # Perform k operations
        for i in range(k):
            # Get the maximum (most negative value)
            max_val = -heapq.heappop(gifts)
            
            # Take sqrt of max value and push back (as negative)
            heapq.heappush(gifts, -math.isqrt(max_val))
        
        # Return total gifts (negate back to positive sum)
        return -sum(gifts)

# TRICK: Max heap simulation using min heap with negation.
# Each iteration: take max, replace with its square root.
# Continue k times. Use heapq for O(log n) operations.
# T(N) = O(k * log n)
# S(N) = O(n)
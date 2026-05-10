class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Koko Eating Bananas: Find the minimum integer speed k to eat all bananas within h hours.
        
        TRICK USED:
        - Binary Search on the Answer: Instead of searching through the input array, we search through the range of possible speeds [1, max(piles)].
        - For each candidate speed (mid), we calculate the total time required and adjust our boundaries.
        - Using math.ceil(p / mid) ensures we account for the fact that Koko cannot eat from two different piles in the same hour.
        
        WHY IT WORKS:
        - The problem has a monotonic property: if Koko can finish at speed 'k', she can also finish at any speed greater than 'k'.
        - This monotonicity allows us to discard half of the remaining speeds in each step, narrowing down to the minimum valid speed.
        - The maximum possible speed required is the size of the largest pile (max(piles)), which would allow her to finish any pile in exactly one hour.
        """
        
        # Initialize binary search range from 1 to the largest pile
        left = 1
        right = max(piles)
        res = right
        
        # Binary search for the minimum viable speed
        while left <= right:
            
            # Calculate candidate speed (mid)
            mid = (left + right) // 2
            
            # Calculate total hours needed at current speed 'mid'
            hours = 0
            for p in piles:
                # Add hours for each pile, rounding up for partial hours
                hours += math.ceil(p / mid)
            
            # If current speed allows finishing within h hours
            if hours <= h:
                # Record this as a potential result and try slower speeds
                res = min(res, mid)
                right = mid - 1
            else:
                # Speed is too slow, must increase the minimum speed
                left = mid + 1
                
        return res

# COMPLEXITY ANALYSIS:
# T(n) = O(n * log(m)) - Time Complexity
#   - n is the number of piles, m is the maximum number of bananas in a pile.
#   - Binary search takes O(log(m)) iterations.
#   - Each iteration involves a linear pass O(n) through the piles to calculate total hours.
#
# S(n) = O(1) - Space Complexity
#   - We only use a constant amount of extra space for pointers and counters.